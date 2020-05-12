from pyschemagen.element_types import TextElement, StringElement, IntElement, FloatElement, BoolElement, \
    TimestampElement, RootElement
from os import mkdir
from os import path


class Parser:
    def __init__(self, data: dict, table_name: str, package_name="db"):
        self._data = data
        self._table_name = table_name
        self._package_name = package_name

    @property
    def _elements(self):
        elements = [RootElement(self._table_name)]
        for k, v in self._data.items():
            if isinstance(v, str):
                if len(v) > 200:  # if the len is too long we'll need to convert it to a text node.
                    elements.append(TextElement(k, v))
                else:
                    elements.append(StringElement(k, v))
            elif isinstance(v, bool):
                elements.append(BoolElement(k, v))
            elif isinstance(v, int):
                # ex: 942935400000
                # this is a very crude system... probably will need improvement down the road.
                if len(str(v)) == 12 or "timestamp" in k.lower():
                    elements.append(TimestampElement(k, v))
                else:
                    elements.append(IntElement(k, v))
            elif isinstance(v, float):
                elements.append(FloatElement(k, v))

        return elements

    def pretty_print(self):
        return '\n\t'.join([e.eval() for e in self._elements])

    @property
    def _db_config_src(self) -> str:
        return """from orator import DatabaseManager, Model

config = {
    'development': {
        'driver': 'sqlite',
        'database': './test.db'  # feel free to change this. 
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)"""

    @property
    def _package_init_src(self):
        return f"from {self._package_name} import config\n"

    @property
    def _model_name(self):
        return self._table_name.title()

    @property
    def _model_src(self) -> str:
        return f"""from orator import Model

class {self._model_name}(Model):
    __guarded__ = ['id']
"""

    @property
    def _import_module_src(self):
        return f"""from {self._package_name}.{self._model_name.lower()} import {self._model_name}
import re


def to_snake_case(data: dict) -> dict:
    output = {{}}
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    for k, v in data.items():
        k = pattern.sub('_', k).lower()
        output[k] = v
    return output


def import_into_{self._model_name.lower()}(data:dict):
    data = to_snake_case(data)    
    model = {self._model_name}()
    model.create(data)
    model.save()
"""

    @property
    def _schema_module_src(self):
        return f"""from orator import Schema
from {self._package_name}.config import db


if __name__ == "__main__": 
    schema = Schema(db)
    {self.pretty_print()}    
"""

    def write_all(self):
        # make the dir for our new module if it does not exist already.
        root_module_path = f"./{self._package_name}"

        if not path.exists(root_module_path):
            mkdir(root_module_path)

        # we just make a module file.
        with open(f"{root_module_path}/__init__.py", 'w') as f:
            f.write(self._package_init_src)

        with open(f"{root_module_path}/config.py", 'w') as f:
            f.write(self._db_config_src)

        # create our model file
        with open(f"{root_module_path}/{self._model_name.lower()}.py", 'w') as f:
            f.write(self._model_src)

        with open(f"{root_module_path}/schema.py", 'w') as f:
            f.write(self._schema_module_src)

        with open(f"{root_module_path}/import.py", "w") as f:
            f.write(self._import_module_src)

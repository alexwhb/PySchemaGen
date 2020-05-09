import re
from typing import Optional


class BaseElement:
    def __init__(self, key=None, val=None):
        self._key = key
        self._val = val

    @property
    def field_name(self) -> str:
        """Convert our key to snake case instead of camel, so that we are following the norm with db schemas"""
        pattern = re.compile(r'(?<!^)(?=[A-Z])')
        return pattern.sub('_', self._key).lower()

    def eval(self):
        pass


class RootElement(BaseElement):
    def eval(self):
        return f"with schema.create('{self.field_name}') as table:" \
               f"\n\ttable.increments('id')"


class TextElement(BaseElement):

    def eval(self):
        return f"table.text('{self.field_name}')"


class StringElement(BaseElement):

    def eval(self):
        return f"table.string('{self.field_name}')"


class IntElement(BaseElement):

    def eval(self):
        return f"table.integer('{self.field_name}')"


class DateElement(BaseElement):

    def eval(self):
        return f"table.datetime('{self.field_name}')"


class FloatElement(BaseElement):

    def eval(self):
        return f"table.float('{self.field_name}')"


class BoolElement(BaseElement):

    def eval(self):
        return f"table.boolean('{self.field_name}')"


class TimestampElement(BaseElement):

    def eval(self):
        # if self.child:
        #     self.child.eval()
        return f"table.timestamp('{self.field_name}')"


class DictElement(BaseElement):
    def eval(self):
        print("Warning we are not implementing dicts right now")
        # if isinstance(self.child, list):
        #
        #     for c in self.child:
        #         c.eval()
        #
        # return self.child


class ArrayElement(BaseElement):

    def eval(self):
        print("Warning we are not implementing arrays right now")

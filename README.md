# PySchemaGen

This is a very rudimentary project that allows you to generate
a flat but complex schema off of a flat json dict.

example: 
```python
from pydbgen import Parser

if __name__ == '__main__':
    dictionary_data = {
        "keyOne": "value",
        "keyTwo": 1,
        "keyThree": False,
        "keyFour": 1.5,
    }
    
    p = Parser(data=dictionary_data, table_name="MyTable")
    p.write_all(root_module_path="./my_module")
``` 


this above method will generate a new module with [orator](https://orator-orm.com/) schema definition and model definition 
automatically generated from the dict that you passed in. Currently this only works with single level dictionaries, 
though I might build on this in the future. 

it will output a directory structure like this: 
```
my_module
|__ __init__.py
|__ config.py
|__ import.py
|__ schema.py
|__ mytable.py
```

* **config.py** sets up your db connection for you
* **import.py** sets up a rudimentary import function that will convert the dictionary into the new schema format. 
* **schema.py** sets up your db schema. 
* **mytable.py** is the model file for your database. 

### Dependencies
This project assumes you have Orator-Orm installed. If you have that you are good to go. 


feel free to fork and send PRs my way. :) 
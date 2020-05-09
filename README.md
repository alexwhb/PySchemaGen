# JSON Orator Schema Generator (JOSG)

This is a very rudimentary project that allows you to generate
a flat but complex schema off of a flat json dict.

example: 
```python
from parser import Parser

if __name__ == '__main__':
    dictionary_data = {
        "keyOne": "value",
        "keyTwo": "value",
        "keyThree": "value",
        "keyFour": "value",
    }
    
    p = Parser(data=dictionary_data, table_name="MyTable")
    p.write_all(root_module_path="./my_module")

``` 

this above method will generate a new module with [orator](https://orator-orm.com/) schema definition and model definition 
automatically generated from the dict that you passed in. Currently this only works with single level dictionaries, 
though I might build on this in the future. 

feel free to fork and send PRs my way. :) 
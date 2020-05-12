# PySchemaGen

This is a very rudimentary project that allows you to generate
a flat but complex schema off of a flat json dict.

I built this because I write a lot of data import systems in my 
free time just scraping stuff from public APIs or the web and I find it truly tedious
to write schemas all the time when im not building anything production ready. 
so this is just a system to fast track that process by spitting out a schema based on a dictinary. 

#### How do I use it?

```python
from pyschemagen import Parser

if __name__ == '__main__':
    dictionary_data = {
        "keyOne": "value",
        "keyTwo": 1,
        "keyThree": False,
        "keyFour": 1.5,
    }
    
    # explicitly typing the param names like this is not required. 
    # I'm just doing it to make it clear what goes where. 
    
    p = Parser(data=dictionary_data, table_name="MyTable")
    p.write_all()
``` 


This above method will generate a new module with [orator](https://orator-orm.com/) schema definition and model definition 
automatically generated from the dict that you passed in. Currently this only works with single level dictionaries, 
though I might build on this in the future. 

It will output a directory structure like this: 
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

Currently the schema makes everything nullable other than the primary key and created_at/updated_at fields. 
This is to insure that the import of your data is not having errors, but you are free to adjust the schema as you see fit. 
Ideally down the road I'd like to make this system able to accept a list of dicts so that it can evaluate essentially the 
lowest common denominator of data between them, but that will have to come later. 

### Dependencies
This project assumes you have Orator-Orm installed. If you have that you are good to go. 


Feel free to fork and send PRs my way. :) 
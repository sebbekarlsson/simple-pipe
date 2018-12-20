# Pipe Function Composition for Python!
> pipe methods in Python!

## Usage:

    from simple_pipe.methods import pipe
    
    
    pipe([<list_of_methods>], <your-input>)

    # your input variable will go through all the methods,
    # and then the pipe method will return the final modified variable.

## Example:

    from simple_pipe.methods import pipe


    myvar = 'hello world'

    print(pipe([lambda x: x.title(), lambda x: x.replace(' ', '')], myvar))

    >> HelloWorld


> You can also create re-usable `compositions` like this _(note the `compose=True` flag)_:

    objects = [{'name': 'John'}, {'name': 'Lisa'}, {'Name': 'Eric'}]

    composition = pipe([
        lambda x: safe_set_attribute(x, 'age', 21),
        lambda x: safe_set_attribute(x, 'color', 'green')
    ], compose=True)

    [composition.execute(obj) for obj in objects]

    print(objects)

    >> [
        {'name': 'John', 'age': 21, 'color': 'green'},
        {'name': 'Lisa', 'age': 21, 'color': 'green'},
        {'Name': 'Eric', 'age': 21, 'color': 'green'}
    ]


## Install
> Run:

    pip install simple-pipe

> or ...

* Clone down the repository

> And then execute:

    python setup.py install

## Running Unit Tests

    pip install pytest
    pytest .

## License
> [GPL 3.0](gpl-3.0.md)

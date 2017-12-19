# Pipe Function Composition for Python!
> pipe methods in Python!

## Usage:

    from simple_pipe.methods import pipe
    
    
    pipe(<your_input>, [<list_of_methods>])

    # your input variable will go through all the methods,
    # and then the pipe method will return the final modified variable.

## Example:

    from simple_pipe.methods import pipe


    myvar = 'hello world'

    print(pipe(myvar, [lambda x: x.title(), lambda x: x.replace(' ', '')]))

    >> HelloWorld


## Install
* Run:

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

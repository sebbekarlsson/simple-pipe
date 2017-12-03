# Pipe Function Composition for Python!
> pipe methods in Python!

## Usage:

    from pypipe.methods import pipe
    
    
    pipe(<your_input>, [<list_of_methods>])

    # your input variable will go through all the methods,
    # and then the pipe method will return the final modified variable.

## Example:

    from pypipe.methods import pipe


    myvar = 'hello world'

    print(pipe(myvar, [lambda x: x.title(), lambda x: x.replace(' ', '')]))

    >> HelloWorld


## Install
* Clone down the repository

> And then execute:

    python setup.py install

## Running Unit Tests

    pip install pytest
    pytest .

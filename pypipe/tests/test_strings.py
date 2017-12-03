from pypipe.methods import pipe


def test_hello_world():
    myvar = 'hello world'

    myvar = pipe(myvar, [lambda x: x.title(), lambda x: x.replace(' ', '')])

    assert myvar == 'HelloWorld'

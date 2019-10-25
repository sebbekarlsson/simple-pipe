from simple_pipe import pipe


def test_hello_world():
    myvar = 'hello world'

    myvar = pipe(lambda x: x.title(), lambda x: x.replace(' ', ''))(myvar)

    assert myvar == 'HelloWorld'

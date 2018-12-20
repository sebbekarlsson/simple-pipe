from simple_pipe.methods import pipe


def safe_set_attribute(obj, attr, value):
    obj[attr] = value

    return obj


def test_hello_world():
    myvar = 'hello world'

    composition = pipe(
        [lambda x: x.title(), lambda x: x.replace(' ', '')], compose=True
    )

    assert composition.execute(myvar) == 'HelloWorld'
    assert composition.execute('john doe 256') == 'JohnDoe256'


def test_objects():
    objects = [{'name': 'John'}, {'name': 'Lisa'}, {'Name': 'Eric'}]

    composition = pipe([
        lambda x: safe_set_attribute(x, 'age', 21),
        lambda x: safe_set_attribute(x, 'color', 'green')
    ], compose=True)

    for obj in objects:
        composition.execute(obj)
        assert obj['age'] == 21
        assert obj['color'] == 'green'

from simple_pipe import pipe


myvar = 'hello world'

print(pipe(lambda x: x.title(), lambda x: x.replace(' ', ''))(myvar))


objects = [{'name': 'John'}, {'name': 'Lisa'}, {'Name': 'Eric'}]

def safe_set_attribute(x, name, val):
    x[name] = val
    return x

composition = pipe(
    lambda x: safe_set_attribute(x, 'age', 21),
    lambda x: safe_set_attribute(x, 'color', 'green')
)

objects = [composition(obj) for obj in objects]

print(objects)

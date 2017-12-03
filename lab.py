from pypipe.methods import pipe


myvar = 'hello world'

print(pipe(myvar, [lambda x: x.title(), lambda x: x.replace(' ', '')]))

from functools import partial


pipe = lambda *args: partial(reduce, lambda x, g: g(x), args)

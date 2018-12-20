from functools import reduce


class Pipe(object):
    def __init__(self, methods):
        self.methods = methods

    def execute(self, arg):
        return reduce(
            lambda value,
            function: function(value), self.methods, arg
        )


def pipe(methods, arg=None, compose=False):
    p = Pipe(methods)

    return p if compose else p.execute(arg)

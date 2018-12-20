from functools import reduce


def pipe(_arg, methods):
    return reduce(lambda value, function: function(value), methods, _arg)

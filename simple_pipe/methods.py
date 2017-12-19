def pipe(_arg, methods):
    if len(methods):
        _arg = methods[0](_arg)
        methods.pop(0)
        return pipe(_arg, methods)

    return _arg

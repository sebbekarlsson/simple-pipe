def pipe(_arg, args):
    if len(args) > 0:
        _arg = args[0](_arg)
        args.pop(0)
        return pipe(_arg, args)
    else:
        return _arg

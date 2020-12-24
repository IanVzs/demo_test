def hello(a, ba=None, bc=..., **kwargs):
    import pdb; pdb.set_trace()
    print(bc or ba)

hello('1', "你好",)

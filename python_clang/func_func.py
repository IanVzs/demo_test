def a():
    def b():
        return "b"
    print(locals())

w = a()
print(w)

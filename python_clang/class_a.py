class A:
    a = 1
    def hi(self, w):
        print(self.a)
        print(w)
if "__main__" == __name__:
    A().hi("w is me")

class A:
    a = 1
    def __init__(self):
        self.ini = 'ini'

    def hi(self, w):
        print(self.a)
        print(w)

    @classmethod
    def cm(self):
        print(f"in www: {self.ini}")

    @classmethod
    def cm2(hi):
        print(f"in www2: asd")

if "__main__" == __name__:
    A().hi("w is me")
    A.cm2()
    A().cm()

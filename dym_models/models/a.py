from models.base import BaseModel
class A(BaseModel):
    def go(self):
        self.a = 'a'
        print(self.a)

def go():
    a = 'a'
    print(a)

def get_appid():
    return "a"

def test_rewrite():
    sign = False
    print("test_rewrite", sign)

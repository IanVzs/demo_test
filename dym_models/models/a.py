from models.base import BaseModel
class A(BaseModel):
    def go(self):
        self.a = 'a'
        print(self.a)

def go():
    a = 'a'
    print(a)

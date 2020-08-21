from models.base import BaseModel
class A(BaseModel):
    def go(self):
        self.a = 'b'
        print(self.a)

def go():
    a = 'b'
    print(a)

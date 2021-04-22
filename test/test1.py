class Link:
    content = ''
    _next = None

class LinkedList:
    head = None
    last = None
    def append(self, _i: str):
        if not self.last:
            self.last = Link()
            self.last.content = _i
            self.head = self.last
        else:
            _tmp = Link()
            _tmp.content = _i
            self.last._next = _tmp
        
    def print(self):
        _loop = self.head
        while 1:
            print(_loop.content)
            if not _loop._next:
                break
            _loop = _loop._next

if "__main__" == __name__:
    linkedlist = LinkedList()
    linkedlist.append("abc")
    linkedlist.append("xyz")
    linkedlist.print()

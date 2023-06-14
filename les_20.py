print(id(1), type(1))
print(id(id), type(id))


class A:
    def public(self):
        return 42
    
    def _private(self):
        return 'test'
    
    def __protect(self):
        return True
    
a = A()
print(a.public())
print(a._private())
print(a._A__protect())
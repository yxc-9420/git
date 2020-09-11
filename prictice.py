class A:
    def show(self):
        print('is A')
    def __call__(self, *args, **kwargs):
        print('call A')

class B(A):
    def new_decoretor(a_func):
        def doFun(self):
            print('before')
            a_func(self)
            print('after')
        return doFun
    @new_decoretor
    def show(self):
        print('is B')
    def __call__(self, *args, **kwargs):
        print('call B')

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
            

if __name__ == '__main__':
    b = B()
    b.show()
    b()
    b.__class__ = A
    b.show()
    b()
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
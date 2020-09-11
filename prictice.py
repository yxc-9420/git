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


if __name__ == '__main__':
    b = B()
    b.show()
    b()
    b.__class__ = A
    b.show()
    b()
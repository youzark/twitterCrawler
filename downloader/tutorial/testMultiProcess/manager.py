#!/usr/bin/env python
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager, BaseProxy
import operator

class Foo:
    def f(self):
        print("you called Foo.f()")
    def g(self):
        print('you called Foo.g()')
    def _h(self):
        print('you called Foo._h()')

def baz():
    for i in range(10):
        yield i*i

class GeneratorProxy(BaseProxy):
    _exposed_ = ['__next__']
    def __iter__(self):
        return self
    def __next__(self):
        return self._callmethod("__next__")

def getOperatorModule():
    return operator




class MyManager(BaseManager):
    pass

MyManager.register("Foo1",Foo)
MyManager.register("Foo2",Foo,exposed=('g','_h'))
MyManager.register("baz",baz,proxytype=GeneratorProxy)
MyManager.register("operator",getOperatorModule)

def test():
    manager = MyManager()
    manager.start()

    print("-"*20)

    f1 = manager.Foo1()
    f1.f()
    f1.g()
    assert not hasattr(f1,"_h")

    print("-"*20)

    f2 = manager.Foo2()
    f2.g()
    f2._h()
    assert not hasattr(f2,"f")

    print("-"*20)
    it = manager.baz()
    for i in it:
        print("<%d>" % i, end = ' ')
    print()
    print("-"*20)

    op = manager.operator()
    print('op.add(23, 45) =', op.add(23, 45))

if __name__ == "__main__":
    test()
















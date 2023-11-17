class Base1:
    def __init__(self):
        self.str1 = "base1"
        print("base1")


class Base2:
    def __init__(self):
        self.str1 = "base2"
        print("base2")


class Derived(Base1,Base2):
    def __init__(self):
        # Base1.__init__(self)
        # Base2.__init__(self)
        print("derived")


obj = Derived()

class BaseClass1:

    def method(self):
        print("BaseClass1")

class BaseClass2:
    def method(self):
        print("BaseClass2")

class MyClass(BaseClass1, BaseClass2):
    def method(self):
        super().method()

c = MyClass()

c.method()




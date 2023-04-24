import pandas as pd


class MyClass(object):

    def __init__(self, some_value: int):
        self.value = some_value

    def one_more_function(self, another_value):
        print(another_value)


myObject = MyClass(45)
myObject.one_more_function(2)
my__object2 = MyClass(324)

print('ok')


def some_foo():
    """
    """
    pass

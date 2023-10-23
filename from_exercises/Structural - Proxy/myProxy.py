"""
Scrivere una classe MyProxy che è il proxy della classe MyClass. Ogni volta che viene invocato un metodo di
istanza della classe MyProxy, di fatto viene invocato l’omonimo metodo di istanza di MyClass. NON deve
essere usata l’ereditarietà.
• Si assuma che __init__ di MyClass prenda in input un argomento x e che il comportamento dei suoi
metodi di istanza dipenda dal valorie di x passati a __init__.
"""

class myClass:
    def __init__(self, x):
        self.value = x
        print('my variable is a ', type(self.value))

    def add10(self):
        self.value += 10

    def add_string(self):
        self.value += " Hello World!"


class myProxy:
    def __init__(self, value):
        self.__implementation = myClass(value)

    def __getattr__(self, name):
        return getattr(self.__implementation, name)

    def available_functions(self):
        implementation_attrs = dir(self.__implementation)
        method_names = [attr for attr in implementation_attrs if callable(getattr(self.__implementation, attr))]
        return method_names

    def print_value(self):
        print('the value is now: ', self.__implementation.value)

use = myProxy(5)
print(use.available_functions())
use.add10()
use.print_value()

>>my variable is a  <class 'int'>
>>['__class__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'add10', 'add_string']
>>the value is now:  15

# esempio di utilizzo 1
def decorator(aClass): ...

@decorator
class C: ...

# esempio di utilizzo 2
def decorator(aClass): ...

class C: ...
C = decorator(C)

# esempio concreto
def count(aClass):
    aClass.numInstances = 0
    return aClass

@count
class Spam:
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

class Sub(Spam):
    pass

class Other(Spam):
    pass


# OUTPUT
>>> from classdec0.py import Spam, Sub,
Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
3
>>> print(sub.numInstances)
3
>>> print(other.numInstances)
3


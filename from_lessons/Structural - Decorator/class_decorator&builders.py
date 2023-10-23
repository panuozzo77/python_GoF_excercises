"""
Ogni classe ha una variabile numInstances tranne Sub. 

Quando viene creato un oggetto di tipo Spam è invocato __init__ della classe base Spam quindi incrementa solo numInstances di Spam .

Quando viene creato un oggetto di tipo Sub è invocato __init__ della classe base Spam quindi incrementa solo numInstances di Spam .

Quando viene creato un oggetto di tipo Other, viene invocato il *suo costruttore* ed è incrementato numInstances di Other.
"""
def count(aClass):
	aClass.numInstances = 0
	return aClass

@count
class Spam:
	def __init__(self):
		Spam.numInstances =Spam.numInstances + 1

@count
	class Sub(Spam):
		pass

@count
class Other(Spam):
	def __init__(self):
		Other.numInstances =Other.numInstances + 1

>>> from classdec1.py import Spam, Sub, Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
2
>>> print(sub.numInstances)
0
>>> print(other.numInstances)
1

# ----------------------------------------------------------------------------------------------------------------
"""
Ogni classe ha una variabile numInstances tramite il decoratore. 

A differenza del codice precedente, ora il costruttore utilizza un metodo di *classe* che prende la variabile numInstances (che però hanno tutte le classi e sottoclassi) e la addiziona

Quando viene creato un oggetto di tipo Spam è invocato __init__ della classe base Spam quindi incrementa solo numInstances di Spam .

Quando viene creato un oggetto di tipo Sub è invocato __init__  incrementa solo numInstances di Sub .

Quando viene creato un oggetto di tipo Other è invocato __init__  incrementa solo numInstances di Sub .
"""

def count(aClass):
	aClass.numInstances = 0
	return aClass

@count
class Spam:
	@classmethod
	def count(cls):
		cls.numInstances+=1
	
	def __init__(self):
		self.count()

@count
class Sub(Spam):
	pass

@count
class Other(Spam):
	pass

>>> from classdec2.py import Spam, Sub, Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
1
>>> print(sub.numInstances)
1
>>> print(other.numInstances)
1
>>> other=Other()
>>> print(other.numInstances)
2
>>> print(spam.numInstances)
1
>>> print(sub.numInstances)
1

# ----------------------------------------------------------------------------------------------------------------
"""
Qui invece abbiamo ridefinito il costruttore, utilizzandone ben 2 in una sola chiamata, osserviamo bene:

Possiamo vedere che ogni classe possiede una propria variabile numInstances ma, 
ad ogni chiamata del costruttore viene incrementata sia quella delle sottoclassi che quella della classe genitore.

"""
def count(aClass):
	aClass.numInstances = 0
	oldInit=aClass.__init__
	
	def __newInit__(self,*args,**kwargs):
		aClass.numInstances+=1
		oldInit(self,*args,**kwargs)

#questo è il vecchio init
	aClass.__init__=__newInit__
		return aClass

@count
class Spam:
	pass

@count
class Sub(Spam):
	pass

@count
class Other(Spam):
	pass

>>> from classdec3.py import Spam, Sub, Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
3
>>> print(sub.numInstances)
1
>>> print(other.numInstances)
1
>>> other=Other()
>>> print(other.numInstances)
2
>>> print(spam.numInstances)
4
>>> print(sub.numInstances)
1

"""
- Nella classe Borg tutte le istanze sono diverse ma condividono lo stesso stato.
- Lo stato è condiviso dall’attributo shared_state e tutte le nuove istanze di Borg avranno lo stesso stato così come è definito dal metodo __new__
- In genere, lo stato di un’istanza è memorizzato nel dizionario __dict__ proprio dell’istanza. 
  Nel codice in basso assegnamo la variabile di classe shared_state e tutte le istanze create
"""

class Borg():
	_shared_state = {}
	
	def __new__(cls, *args, **kwargs):
		obj = super().__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._shared_state
		return obj

#eseguiamo

class Child(borg):
	pass

>>>borg = Borg()
>>>another_borg = Borg()
>>>borg is another_borg
False
>>>child = Child()
>>>borg.only_one_var = "I'm the only one var"
>>>child.only_one_var
I'm the only one var

# Se volessi definire una sottoclasse di Borg con un altro stato condiviso dobbiamo resettare _shared_state nella sottoclasse come segue

class AnotherChild(Borg):
	_shared_state = {}

>>>another_child = AnotherChild()
>>>another_child.only_one_var
AttributeError: has no attribute 'shared_state'  #in questo modo non trova gli stessi valori definiti nella classe padre

"""
In breve, il Proxy è una classe che funge da "procuratore" per un'altra classe, consentendo di aggiungere funzionalità aggiuntive 
o controlli senza dover modificare direttamente l'oggetto originale. Questo aspetto rende il Proxy un design pattern strutturale, 
in quanto si concentra sulla composizione degli oggetti e sulle relazioni tra di essi, 
anziché sulla creazione di nuovi oggetti o sui comportamenti di esecuzione.
"""
# esempio di proxy che non fa nulla in particolare se non utilizzare esattamente i metodi di Implementation
class Implementation:
	def f(self):
		print("Implementation.f()")
	
	def g(self):
		print("Implementation.g()")
	
	def h(self):
		print("Implementation.h()")

	class Proxy:
		def __init__(self):
			self.__implementation = Implementation()

		# Passa le chiamate ai metodi all’implementazione:
		def f(self): self.__implementation.f() 
		def g(self): self.__implementation.g() 
		def h(self): self.__implementation.h()

		#altrimenti, se vogliamo fare una cosa fina, senza dover ridefinire uno ad uno i metodi con gli stessi nomi:
		def __getattr__(self, name)
			return getattr(self.__implementation, name)


p = Proxy()
p.f(); p.g(); p.h()

"""
Scrvere un decoratore di classe che, se applicato ad una classe la modifica in modo che funzioni come se fosse stata derivata dalla seguente classe base
Le classi derivate da ClasseBase non hanno bisogno di modificare i metodi f() e g() e la variabile varC. Inoltre, quando vengono create le istanze di una
classe derivata queste "nascono" con lo stesso valore di varl settato da __init__ di ClasseBase
"""

class ClasseBase:
    varC = 1000

    def __init__(self):
        self.varl = 10

    def f(self, v):
        print(v * self.varl)

    @staticmethod
    def g(x):
        print(x * ClasseBase.varC)

def classe_derivata_da_ClasseBase(cls):
    class ClasseDerivata(cls, ClasseBase):
        def __init__(self, *args, **kwargs):
            super(ClasseDerivata, self).__init__(*args, **kwargs)
            # Inizializza varl alla stessa maniera di ClasseBase
            self.varl = 10

    return ClasseDerivata

# Definisci il decoratore di classe
def derivata_da_ClasseBase(cls):
    return classe_derivata_da_ClasseBase(cls)

# Usa il decoratore per applicarlo a una classe
@derivata_da_ClasseBase
class MiaClasse:
    pass

# Ora la classe MiaClasse funziona come se fosse derivata da ClasseBase
obj = MiaClasse()
print(obj.varl)  # Output: 10
obj.f(5)         # Output: 50
obj.g(3)         # Output: 3000

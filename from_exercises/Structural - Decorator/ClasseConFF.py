"""
Scrivere un decorator factory che 
-prende in input una classe ClasseConFF e due stringhe funz e ff
-e restituisce un decoratore di classe che:
    - decora una classe in modo tale che se viene invocata funz di fatto al posto di funz viene invocata la funzione ff della classe ClasseConFF.
"""
def decorator_factory(classe, funz, ff):
    def class_decorator(cls):
        # Ottieni una reference al metodo 'ff' dalla classe 'ClasseConFF'
        ff_method = getattr(classe, ff)
        # Sostituisci il metodo 'funz' con il metodo 'ff' nella classe da decorare
        setattr(cls, funz, ff_method)
        return cls

    return class_decorator


# Esempio di classe 'ClasseConFF'
class ClasseConFF:
    def funz(self):
        print("Metodo funz di ClasseConFF")

    def ff(self):
        print("Metodo ff di ClasseConFF")


# Applica il decoratore factory per decorare una classe
@decorator_factory(ClasseConFF, 'funz', 'ff')
class MiaClasse:
    pass


# Ora la classe 'MiaClasse' sostituisce il metodo 'funz' con il metodo 'ff' di 'ClasseConFF'
obj = MiaClasse()
obj.funz()  # Chiama il metodo 'ff' di 'ClasseConFF' invece di 'funz'

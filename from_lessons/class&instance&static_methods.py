from typing import Self
from datetime import date

class Calculator :
    def __init__(self, version: int):
        self.version = version

    #metodo di istanza. Il valore è preso dal singolo oggetto che verrà istanziato
    def description(self):
        print(f'Currently running Calculator on version: {self.version}')

    #questo metodo è statico. Può essere usato da qualsiasi istanza e non influenzerà nulla nell'oggetto.
    #possiamo anche eliminare self
    #è bene solitamente scrivere @staticmethod su queste funzioni
    #possiamo chiamare il metodo anche direttamente con Calculator.add_numbers senza dover istanziare un oggetto!
    @staticmethod
    def add_numbers(self, *numbers: float) -> float:
        return sum(numbers)

if __name__ == '__main__':
    calc1 = Calculator(10)
    calc2 = Calculator(200)

    calc1.description() #mi aspetto versione 10
    calc2.description() #mi aspetto versione 200

    print(Calculator.add_numbers(10, 20, 30))

# ------------------------------------------------------------------------------------------------------------------- #

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # questo è un metodo che è influenzato dall'istanza
    def description(self) -> str:
        return f'{self.name} is {self.age} years old.'

    @classmethod  # sono riconosciute perché c'è il decoratore e contengono cls (puoi scriverci in realtà quello che vuoi al posto di cls)
    #un metodo di classe "affect" the class
    #un metodo di istanza "affect" the instance (usa self e le variabili già presenti all'interno)
    #un metodo statico può essere anche definito esternamente la classe, non ha nulla a che fare con essa ed ha un comportamento uguale da ogni istanza chiamata se ha gli stessi parametri
    def age_from_year(cls, name: str, birth_year: int) -> Self:
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)  # abbiamo letteralmente creato un secondo costruttore che sfrutta il primo costruttore



if __name__ == '__main__':
    federico = Person.age_from_year('Federico', 2000)
    print(federico.description())

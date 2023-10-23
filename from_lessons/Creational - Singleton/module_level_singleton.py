"""
Tutti i moduli sono per loro natura dei singleton per il modo in cui vengono importati in Python:

1. Se il modulo è già stato importato, questo viene restituito. Altrimenti, dopo aver trovato il modulo, questo viene inizializzato e restituito.
2. Inizializzare il modulo significa eseguire un codice includendo tutti gli assegnamenti a livello del modulo.
3. Quando si importa un modulo per la prima volta, vengono fatte tutte le inizializzazioni. Quando si importa il modulo una seconda volta, Python non esegue l’inizializzazione.
"""
# singleton.py
only_one_var = "I'm only one var"


# module1.py
import singleton
print(singleton.only_one_var)
singleton.only_one_var += " after modification"
import module2


# module2.py
import singleton
print (singleton.only_one_var)


# output
>>>python module1.py
I'm only one var                         # questo proviene dalla stampa a riga 7
I'm only one var after modification      # questo proviene dalla stampa a riga 14

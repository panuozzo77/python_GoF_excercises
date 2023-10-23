"""
if __name__=="__main__":
    it=generaQuadratoInput(100)

    for x in it:
        print("Questo e` il quadrato del numero digitato: ",x)
        

        
    print("Input non valido o l'utente ha forzato l'interruzione dello script:l'iteratore ha smesso di funzionare")
    print("Provo a invocare di nuovo next(it).")
    try:
        next(it)
    except StopIteration:
        print("L'iteratore ha smesso di funzionare")
    
        


I test:
Se digito unn intero maggiore di 100 o qualcosa che non e` un intero, o se interrompo con ctrl+c lo script, il programma
stampa:

Digita un intero--> 
Input non valido o l'utente ha forzato l'interruzione dello script:l'iteratore ha smesso di funzionare
Provo a invocare di nuovo next(it).
L'iteratore ha smesso di funzionare

======================================================
II test:
Se invece eseguo nuovamente lo script e digito gli interi 5,2,10,6,104, il programma stampa:

Digita un intero--> 5
Questo e` il quadrato del numero digitato:  25
Digita un intero--> 2
Questo e` il quadrato del numero digitato:  4
Digita un intero--> 10
Questo e` il quadrato del numero digitato:  100
Digita un intero--> 6
Questo e` il quadrato del numero digitato:  36
Digita un intero--> 104
Input non valido o l'utente ha forzato l'interruzione dello script:l'iteratore ha smesso di funzionare
Provo a invocare di nuovo next(it).
L'iteratore ha smesso di funzionare
"""

def is_valid_integer(input_str):
    try:
        num = int(input_str)
        return num
    except ValueError:
        return None


def generaQuadratoInput(max_value):
    while True:
        try:
            user_input = input("Digita un intero--> ")
            num = is_valid_integer(user_input)

            if num is not None:
                if num > max_value:
                    print("Input non valido: il numero è maggiore di", max_value)
                    return
                else:
                    yield num ** 2
            else:
                print("Input non valido: devi digitare un intero.")
                return
        except KeyboardInterrupt:
            print("L'utente ha forzato l'interruzione dello script.")
            return


if __name__ == "__main__":
    it = generaQuadratoInput(100)

    for x in it:
        print("Questo e` il quadrato del numero digitato:", x)

    print("Input non valido o l'utente ha forzato l'interruzione dello script: l'iteratore ha smesso di funzionare")
    print("Provo a invocare di nuovo next(it).")
    try:
        next(it)
    except StopIteration:
        print("L'iteratore ha smesso di funzionare")

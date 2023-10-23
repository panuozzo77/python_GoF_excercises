"""
Esercizio
- Scrivere il decoratore di funzione decf che fa in modo che venga lanciata l’eccezione TypeError se il numero di argomenti è diverso da due. 
Altrimenti, se la funzione decorata restituisce un risultato, questo viene aggiunto insieme al valore del primo argomento in un file di nome “risultato.txt”.
- Suggerimento: Ricordatevi di convertire a stringa il valore del primo argomento e il risultato quando li scrivete nel file 
e di aprire il file in modo da non cancellare quanto scritto precedentemente nel file. 
"""

def decf(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if(len(args)+len(kwargs)=!2):
			raise TypeError("function must have 2 arguments!")
		else
			result = function(*args, **kwargs)
			#qui continuiamo a scrivere la funzione decoratore
			with open("risultato.txt", "a") as file:
				arg1 = str(args[0])
				result_str = str(result)
	
				file.write(arg1 + " + " result_str + " = " + str(float(arg1) + float(result_str)) + "\n")
			#abbiamo finito la funzione decoratore
		return result
	return wrapper


#ora utilizziamolo seriamente:

def somma(a, b)
	return a + b

try:
	somma(2, 3)
except TypeError as e:
	print(e)

"""
	Universidad Nacional
	EIF203 I-2019
    Autores:
	- Rebecca Garita Gutiérrez        117620191   Martes y Viernes, 10 AM
	- M. Fernanda González Arias      117660980   Martes y Viernes, 10 AM
	- David Alberto Guevara Sánchez   402450355   Martes y Viernes, 10 AM
	- Luis David Villalobos González  117540697   Martes y Viernes, 10 AM
    Comparacion de tiempo de corrida
    Karatsuba_Python
"""

from knum import KNum
from num import Num
import timeit

def tocomma(n):
	"""
		Reemplaza "." por "," 
	"""
	return str(n).replace(".",",")

if __name__=="__main__":
	numbers = [Num(x) for x in range(100, 1000000, 150)]
	Knumbers = [KNum(x) for x in range(100, 1000000, 150)]
	with open("../data/TiempoCorrida_Natural_Karatsuba.csv","w")as file:
		file.write("n;natural;karatsuba\n")
		for i in range(len(numbers)):
			print("Nueva iteracion...")
			time_natural = timeit.timeit("numbers[i] * numbers[i]", globals=globals(), number=1)
			time_karatsuba = timeit.timeit("Knumbers[i] * Knumbers[i]", globals=globals(), number=1) 
			file.write(f"{i};{tocomma(time_natural)};{tocomma(time_karatsuba)}\n")
	print("Listo...")
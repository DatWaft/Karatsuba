"""
Autores:
  - Rebecca Garita Gutiérrez        117620191   Martes y Viernes, 10 AM
  - David Alberto Guevara Sánchez   402450355   Martes y Viernes, 10 AM
  - M. Fernanda Gonzáles Arias      117660980   Martes y Viernes, 10 AM
  - Luis David Villalobos Gonzáles  117540697   Martes y Viernes, 10 AM
"""

from num import Num

class KNum(Num):
	def karatsuba(self, knum):
		if isinstance(knum, int) or isinstance(knum, str) or isinstance(knum, list):
			knum = KNum(knum, self.base, self.max_length)
		if not isinstance(knum, KNum): raise Exception("'knum' no es de un tipo valido.")

		max_length = max(self.max_length, knum.max_length)
		base = self.base

		if self.base != knum.base:
			knum = KNum(knum.value, base, max_length)

		# Caso base
		if self.size <= 1 or knum.size <= 1:
			return KNum(self.value * knum.value, base, max_length)

		# Caso recursivo
		n = max(self.size, knum.size)
		m = n//2

		x1, x0 = self.cut(m)
		y1, y0 = knum.cut(m)

		z0 = x0.karatsuba(y0)
		z2 = x1.karatsuba(y1)

		z1 = (x1 + x0).karatsuba(y1 + y0) - z2 - z0

		return (z2 << (2*m)) + (z1 << m) + z0


	# Métodos de operación.
	def cut(self, i):
		t = super().cut(i)
		return KNum.copy(t[0]), KNum.copy(t[1])

	def add(self, knum):
		return KNum.copy(super().add(knum))

	def invert(self):
		return KNum.copy(super().invert())

	def sub(self, knum):
		return KNum.copy(super().sub(knum))
	
	def mul(self, knum):
		return KNum.copy(self.karatsuba(knum))

	def pow(self, i):
		return KNum.copy(super().pow(i))

	def div(self, knum):
		t = super().div(knum)
		return KNum.copy(t[0]), KNum.copy(t[1])

	def rshift(self, i): #mueve a la derecha
		return KNum.copy(super().rshift(i))
	
	def lshift(self, i): # mover a la izquierda
		return KNum.copy(super().lshift(i))

	def __str__(self):
		# Cuando se convierte el objeto a un 'str'.
		# Es lo que se imprime cuando uno hace print('objeto').
		return f"KNum({self.string})[{self.base}]"
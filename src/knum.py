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
		if self.size < 1 or knum.size < 1:
			return super().mul(knum)

		n = max(self.size, knum.size)
		m = n//2

		x1 = self / base**m
		x0 = self % base**m

		y1 = knum / base**m
		y0 = knum % base**m

		z0 = x0*y0
		z2 = x1*y1

		z1 = (x0 + x1)*(y1 + y0) - z2 - z0

		return z2*base**(2*m) + z1*base**m + z0


	# Métodos de operación.
	def add(self, num):
		return KNum.copy(super().add(num))

	def invert(self):
		return KNum.copy(super().invert())

	def sub(self, num):
		return KNum.copy(super().sub(num))
	
	def mul(self, num):
		return KNum.copy(super().mul(num))

	def pow(self, i):
		return KNum.copy(super().pow(i))

	def div(self, num):
		t = super().div(num)
		return KNum.copy(t[0]), KNum.copy(t[1])

	def rshift(self, i):
		return KNum.copy(super().rshift(i))
	
	def lshift(self, i):
		return KNum.copy(super().lshift(i))

	def __str__(self):
		# Cuando se convierte el objeto a un 'str'.
		# Es lo que se imprime cuando uno hace print('objeto').
		return f"KNum({Num.list_to_string(self._value)})[{self.base}]"

if __name__ == "__main__":
	x = KNum(1233)
	y = KNum(3244)

	print(f"x = {x}")
	print(f"y = {y}")
	print(f"x*y = {x*y}")
	print(f"x.value * y.value = {x.value * y.value}")
	print(f"x.karatsuba(y) = {x.karatsuba(y)}")
from num import Num

class KNum(Num):
	def karatsuba(self):
		pass

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
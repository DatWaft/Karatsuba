from num import Num

class KNum(Num):
	def __str__(self):
		# Cuando se convierte el objeto a un 'str'.
		# Es lo que se imprime cuando uno hace print('objeto').
		return f"KNum({Num.list_to_string(self._value)})[{self.base}]"

	def karatsuba(self):
		pass
class Num:
	"""
	La clase 'Num' simula un número de cualquier base entre 2 y 36.
	Esta clase contiene 3 atributos:
		- value: es una 'list' de 'int's en base 10.
		- max_length: es un 'int' que especifíca el número máximo de elemento que puede tener 'value'.
		- base: es un 'int' que contiene en qué base está 'value'.
	"""
	# Constantes.
	DEFAULT_BASE = 10
	DEFAULT_LENGTH = 16
	CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyz'


	# Método constructor.
	def __init__(self, value, base = DEFAULT_BASE, max_length = DEFAULT_LENGTH):
		"""
		El constructor de la clase 'Num'.
		El parametro 'value' acepta 'int', 'str' y 'list'.
		Si el parametro 'value' es 'int' el parametro será convertido a la base especificada.
		El parametro 'base' especifica la base del Num, y acepta valores entre 2 y 36.
		El parametro 'length' especifica el largo máximo que puede tener el valor dentro del Num, no puede ser menor a 1.
		"""
		if base > 36 or base < 2: raise Exception("Base invalida. (2 - 36)")
		if max_length < 1: raise Exception("Largo máximo inválido, no puede ser menor a 1.")

		self.base = base
		self.max_length = max_length

		if isinstance(value, int):
			self.value = Num.int_to_list(value, base)
		elif isinstance(value, str):
			self.value = [int(x, base) for x in value]
		elif isinstance(value, list):
			self.value = value
		else:
			raise Exception("'value' es un objeto inválido.")
		
		if len(self.value) > max_length: raise Exception("'value' es demasiado grande.")
		
		self.value = [0 for i in range(self.max_length - len(self.value))] + self.value


	# Métodos que devuelven información.
	def getValue(self):
		# Convierte 'value' a un int en base 10.
		return int(Num.list_to_string(self.value), self.base)

	def getSize(self):
		# Devuelve el número de valores que tiene 'value' sin contar los 0s a la izquierda.
		return len(Num.list_to_string(self.value))


	# Métodos 'static'.
	@staticmethod
	def list_to_string(a):
		s = ''
		flag = False
		for i in a:
			if not flag and i != 0:
				flag = True
				s += Num.CHARACTERS[i]
			elif flag:
				s += Num.CHARACTERS[i]
		if not s:
			s = Num.CHARACTERS[0]
		return s

	@staticmethod
	def int_to_list(i, base):
		i = abs(i)
		l = []
		while i != 0:
			l = [i % base] + l
			i = i//base
		return l


	# Métodos de operación.
	def add(self, num):
		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if self.max_length != num.max_length: raise Exception("El atributo 'max_length' es diferente en los dos 'Num'.")
		if self.base != num.base: raise Exception("La base de los dos 'Num' es diferente.")

		q = []
		r = 0
		for i,j in zip(self.value[::-1], num.value[::-1]):
			q = [(i + j + r) % self.base] + q
			r = (i + j + r) // self.base

		return Num(q, self.base, self.max_length)

	def invert(self):
		new = []
		for i in self.value:
			new += [abs(self.base - 1 - i)]
		new[len(new) - 1] += 1
		return Num(new, self.base, self.max_length)

	def sub(self, num):
		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if self.max_length != num.max_length: raise Exception("El atributo 'max_length' es diferente en los dos 'Num'.")
		if self.base != num.base: raise Exception("La base de los dos 'Num' es diferente.")

		aux = self + ~num
		if(self.getValue() < num.getValue()):
			aux = ~aux
		aux = aux.value[aux.getSize() - self.getSize():]
		return Num(aux, self.base, self.max_length)
	
	def mul(self, num):
		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if self.max_length != num.max_length: raise Exception("El atributo 'max_length' es diferente en los dos 'Num'.")
		if self.base != num.base: raise Exception("La base de los dos 'Num' es diferente.")
		
		cont1 = 0
		res = Num(0, self.base, self.max_length)
		for i in self.value[::-1]:
			cont2 = 0
			aux = Num(0, self.base, self.max_length)
			for j in num.value[::-1]:
				aux += Num(i * j * self.base**cont2, self.base, self.max_length)
				cont2 += 1
			res += Num(aux.getValue() * self.base**cont1, self.base, self.max_length)
			cont1 += 1
		return res

	def pow(self, i):
		if i < 0: raise Exception("El exponente no puede ser menor a 0")
		if i == 0: return Num(1, self.base, self.max_length)

		res = self
		for x in range(1,i):
			res *= self
		return res

	# Operadores sobrecargados.
	def __add__(self, num):
		return self.add(num)

	def __iadd__(self, num):
		self = self + num
		return self

	def __invert__(self):
		return self.invert()

	def __sub__(self, num):
		return self.sub(num)

	def __isub__(self, num):
		self = self - num
		return self

	def __mul__(self, num):
		return self.mul(num)

	def __imul__(self, num):
		self = self * num
		return self

	def __pow__(self, i):
		return self.pow(i)

	def __ipow__(self, i):
		self = self**i
		return self

	def __str__(self):
		return f"Num({Num.list_to_string(self.value)})[{self.base}]"


if __name__ == "__main__":
	n1 = Num(4315, 16)
	print(f"n1 = {n1}")
	print(n1.value)
	print(f"~n1 = {~n1}")
	print((~n1).value)


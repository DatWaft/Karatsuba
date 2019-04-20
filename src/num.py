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
		# convierte 'value' a un int en base 10.
		return int(Num.list_to_string(self.value), self.base)

	def getSize(self):
		# devuelve el número de valores que tiene 'value' sin contar los 0s a la izquierda.
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


	# Métodos de operaciones.
	def add(self, num):
		if not isinstance(num, Num):
			raise Exception("'num' is not a Num.")
		if self.max_length != num.max_length:
			raise Exception("The max length of the two of them is different.")
		if self.base != num.base:
			raise Exception("The base of the two of them is different.")
		base = self.base
		q = []
		r = 0
		for i,j in zip(self.value[::-1], num.value[::-1]):
			q = [(i + j + r) % base] + q
			r = (i + j + r) // base

		return Num(q, base)

	def invert(self):
		new = []
		for i in self.value:
			new += [abs(self.base - 1 - i)]
		new[len(new) - 1] += 1
		return Num(new, self.base, self.max_length)

	def sub(self, num):
		if not isinstance(num, Num):
			raise Exception("'num' is not a Num.")
		if self.max_length != num.max_length:
			raise Exception("The max length of the two of them is different.")
		if self.base != num.base:
			raise Exception("The base of the two of them is different.")
		aux = self + ~num
		if(self.getValue() < num.getValue()):
			aux = ~aux
		aux = aux.value[aux.getSize() - self.getSize():]
		return Num(aux, self.base, self.max_length)
	
	# def mul(self, num):
	# 	if not isinstance(num, Num):
	# 		raise Exception("'num' is not a Num.")
	# 	if self.max_length != num.max_length:
	# 		raise Exception("The max length of the two of them is different.")
	# 	if self.base != num.base:
	# 		raise Exception("The base of the two of them is different.")
		
	# 	res = Num(0)
	# 	cont1 = 0
	# 	for i in self.value[::-1]:
	# 		cont2 = 0
	# 		aux = Num(0)
	# 		for j in num.value[::-1]:
	# 			aux += Num(i * j * self.base**cont2)
	# 			cont2 += 1
	# 		res += Num(aux.getValue() * self.base**cont1)
	# 		cont1 += 1


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

	def __str__(self):
		return f"Num({Num.list_to_string(self.value)})[{self.base}]"

if __name__ == "__main__":
	n1 = Num(15, 16)
	print(n1.value)
	n2 = Num('1d', 16)
	print(n2.value)
	print(f"n1 = {n1}")
	print(f"n2 = {n2}")
	print(f"n1 + n2 = {n1 + n2}")
	n1 += n2
	print(f"n1 = {n1}")
	print(f"n2 = {n2}")


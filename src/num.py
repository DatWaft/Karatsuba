"""
Autores:
  - Rebecca Garita Gutiérrez        117620191   Martes y Viernes, 10 AM
  - David Alberto Guevara Sánchez   402450355   Martes y Viernes, 10 AM
  - M. Fernanda Gonzáles Arias      117660980   Martes y Viernes, 10 AM
  - Luis David Villalobos Gonzáles  117540697   Martes y Viernes, 10 AM
"""

class Num:
	"""
	La clase 'Num' simula un número de cualquier base entre 2 y 36.
	Esta clase contiene 3 atributos:
		- value: es una 'list' de 'int's en base 10.
		- max_length: es un 'int' que especifíca el número máximo de elemento que puede tener 'value'.
		- base: es un 'int' que contiene en qué base está 'value'.
	Todos los números contenidos en la clase 'Num' está en su valor absoluto.
	"""
	# Constantes.
	DEFAULT_BASE = 10
	DEFAULT_LENGTH = 16
	CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyz'


	# Métodos constructores.
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
		
		self.value = [0]*(self.max_length - len(self.value)) + self.value

	@classmethod
	def copy(cls, num):
		# Construtor copia.
		return cls(num.value, num.base, num.max_length)


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
		# Convierte una lista de 'int's a un 'str'.
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
		# Convierte un 'int' base 10 a una 'list' de 'int's en base 'base'.
		i = abs(i)
		l = []
		while i != 0:
			l = [i % base] + l
			i = i//base
		return l


	# Métodos de operación.
	def add(self, num):
		# Devuelve la suma de dos 'Num'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)

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
		# Devuelve el complemento del 'Num'.
		new = []
		for i in self.value:
			new += [abs(self.base - 1 - i)]
		new[len(new) - 1] += 1
		return Num(new, self.base, self.max_length)

	def sub(self, num):
		# Devuelve la resta entre dos 'Num'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)

		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if self.max_length != num.max_length: raise Exception("El atributo 'max_length' es diferente en los dos 'Num'.")
		if self.base != num.base: raise Exception("La base de los dos 'Num' es diferente.")

		aux = self + ~num
		if(self.getValue() < num.getValue()):
			aux = ~aux
		aux = aux.value[aux.getSize() - self.getSize():]
		return Num(aux, self.base, self.max_length)
	
	def mul(self, num):
		# Devuelve la multiplicación de dos 'Num'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)

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
		# Devuelve el 'Num' elevado a la 'i'.
		if not isinstance(i, int): raise Exception("'i' debe ser un 'int'.")
		
		if i < 0: raise Exception("El exponente no puede ser menor a 0")
		if i == 0: return Num(1, self.base, self.max_length)

		res = self
		for x in range(1,i):
			res *= self
		return res

	def div(self, num):
		# Devuelve el 'Num' dividido entre el otro 'Num'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)

		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if self.max_length != num.max_length: raise Exception("El atributo 'max_length' es diferente en los dos 'Num'.")
		if self.base != num.base: raise Exception("La base de los dos 'Num' es diferente.")
		
		cont = 0
		while (num * cont).getValue() < self.getValue():
			cont += 1
		cont -= 1
		return Num(cont, self.base, self.max_length), self - (num * cont)

	def rshift(self, i):
		# Mueve todos los dígitos a la derecha.
		if not isinstance(i, int): raise Exception("'i' debe ser un 'int'.")

		new = Num.copy(self)
		new.value = new.value[:-i]
		new.value = [0]*i + new.value
		return new
	
	def lshift(self, i):
		# Mueve todos los dígitos a la izquierda.
		if not isinstance(i, int): raise Exception("'i' debe ser un 'int'.")

		new = Num.copy(self)
		new.value = new.value[i:]
		new.value = new.value + [0]*i
		return new


	# Operadores sobrecargados.
	def __add__(self, num):
		# Operador '+'.
		return self.add(num)

	def __iadd__(self, num):
		# Operador '+='.
		self = self + num
		return self

	def __invert__(self):
		# Operador '~'.
		return self.invert()

	def __sub__(self, num):
		# Operador '-'.
		return self.sub(num)

	def __isub__(self, num):
		# Operador '-='.
		self = self - num
		return self

	def __mul__(self, num):
		# Operador '*'.
		return self.mul(num)

	def __imul__(self, num):
		# Operador '*='.
		self = self * num
		return self

	def __pow__(self, i):
		# Operador '**'.
		return self.pow(i)

	def __ipow__(self, i):
		# Operador '**='.
		self = self**i
		return self

	def __truediv__(self, num):
		# Operador '/'.
		# Es equivalente al operador '//'.
		return self.div(num)[0]

	def __idiv__(self, num):
		# Operador '/='.
		self = self/num
		return self

	def __floordiv__(self, num):
		# Operador '//='.
		return self.div(num)[0]

	def __ifoordiv__(self, num):
		# Operador '//='.
		self = self//num
		return self

	def __mod__(self, num):
		# Operador '%'.
		return self.div(num)[1]

	def __imod__(self, num):
		# Operador '%='.
		self = self % num
		return self

	def __rshift__(self, i):
		# Operador '>>'.
		return self.rshift(i)

	def __irshift__(self, i):
		# Operador '>>='.
		self = self >> i
		return self

	def __lshift__(self, i):
		# Operador '<<'.
		return self.lshift(i)

	def __ilshift__(self, i):
		# Operador '<<='.
		self = self << i
		return self

	def __str__(self):
		# Cuando se convierte el objeto a un 'str'.
		# Es lo que se imprime cuando uno hace print('objeto').
		return f"Num({Num.list_to_string(self.value)})[{self.base}]"

	def __int__(self):
		# Convierte el objeto a 'int' base 10.
		return self.getValue()

	def __index__(self):
		# Convierte el objeto a 'int' base 10.
		# Se usa en slices, entre otros.
		return self.getValue()

	def __eq__(self, num):
		# Operador '=='.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)

		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if int(self) == int(num): return True
		return False

	def __ne__(self, num):
		# Operador '!='.
		return not self == num
	
	def __lt__(self, num):
		# Operador '<'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)

		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if int(self) < int(num): return True
		return False

	def __gt__(self, num):
		# Operador '>'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)

		if not isinstance(num, Num): raise Exception("'num' no es de tipo 'Num'.")
		if int(self) > int(num): return True
		return False

	def __le__(self, num):
		# Operador '<='.
		return not self > num

	def __ge__(self, num):
		# Operador '>='.
		return not self < num
	

if __name__ == "__main__":
	n1 = Num(189, 16)
	n2 = Num(2, 16)

	print(n1)
	print(n1 >> 1)
	print(n1 << 1)
	print('')
	print(n1 / n2)
	print(n1 // n2)
	print(n1 % n2)

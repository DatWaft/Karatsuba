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
		if base > len(self.CHARACTERS) or base < 2: raise Exception(f"Base invalida. (2 - {len(self.CHARACTERS)})")
		if max_length < 1: raise Exception("Largo máximo inválido, no puede ser menor a 1.")

		self._base = base
		self._max_length = max_length

		if isinstance(value, int):
			self._value = Num.int_to_list(value, base)
		elif isinstance(value, str):
			self._value = [int(x, base) for x in value]
		elif isinstance(value, list):
			self._value = value
		else:
			raise Exception("'value' es un tipo de objeto inválido.")
		
		if len(self._value) > self.max_length:
			self._value = self._value[-self.max_length:]
		else:
			self._value = [0]*(self.max_length - len(self._value)) + self._value

		for i in self._value:
			if i < 0 or i >= base:
				raise Exception("El parametro 'value' es invalido.")

	@classmethod
	def copy(cls, num):
		# Construtor copia.
		return cls(num.value, num.base, num.max_length)


	# Métodos que devuelven información.
	@property
	def value(self):
		# Convierte 'value' a un int en base 10.
		return int(Num.list_to_string(self._value), self.base)

	@property
	def size(self):
		# Devuelve el número de valores que tiene 'value' sin contar los 0s a la izquierda.
		return len(Num.list_to_string(self._value))

	@property
	def base(self):
		# Devuelve la base del Num.
		return self._base

	@property
	def max_length(self):
		# Devuelve el tamaño máximo del vector 'value'.
		return self._max_length

	# Métodos 'static'.
	@staticmethod
	def list_to_string(a):
		# Convierte una lista de 'int's a un 'str'.
		def match(i):
			return Num.CHARACTERS[i]
		s = "".join(map(match, a))
		s = s.lstrip('0')	# Elimina los '0's a la izquierda.

		if not s: # Si el string termina vacío, retornar un '0'.
			return '0'
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
	def cut(self, i):
		return Num(Num.list_to_string(self._value)[:i], self.base, self.max_length), Num(Num.list_to_string(self._value)[i:], self.base, self.max_length)

	def add(self, num):
		# Devuelve la suma de dos 'Num'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)
		if not isinstance(num, Num): raise Exception("'num' no es de un tipo valido.")

		max_length = max(self.max_length, num.max_length)
		base = self.base

		if self.base != num.base:
			num = Num(num.value, base, max_length)

		q = []
		r = 0
		for i,j in zip(self._value[::-1], num._value[::-1]):
			q = [(i + j + r) % base] + q
			r = (i + j + r) // base

		return Num(q, base, max_length)

	def invert(self):
		# Devuelve el complemento del 'Num'.
		new = []
		for i in self._value:
			new += [abs(self.base - 1 - i)]
		return Num(new, self.base, self.max_length)

	def sub(self, num):
		# Devuelve la resta entre dos 'Num'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)
		if not isinstance(num, Num): raise Exception("'num' no es de un tipo valido.")

		max_length = max(self.max_length, num.max_length)
		base = self.base

		if self.base != num.base:
			num = Num(num.value, base, max_length)

		aux = self + ~num
		if(self.value < num.value):
			aux = ~aux
		else:
			aux += 1
		return aux
	
	def mul(self, num):
		# Devuelve la multiplicación de dos 'Num'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)
		if not isinstance(num, Num): raise Exception("'num' no es de un tipo valido.")

		max_length = max(self.max_length, num.max_length)
		base = self.base

		if self.base != num.base:
			num = Num(num.value, base, max_length)
		
		cont1 = 0
		res = Num(0, base, max_length)
		for i in self._value[::-1]:
			cont2 = 0
			aux = Num(0, base, max_length)
			for j in num._value[::-1]:
				aux += Num(i * j * base**cont2, base, max_length)
				cont2 += 1
			res += Num(aux.value * base**cont1, base, max_length)
			cont1 += 1
		return res

	def pow(self, i):
		# Devuelve el 'Num' elevado a la 'i'.
		if not isinstance(i, int): raise Exception("'i' debe ser un 'int'.")
		
		if i < 0: raise Exception("El exponente no puede ser menor a 0")
		if i == 0: return Num(1, self.base, self.max_length)

		res = self
		for _ in range(1,i):
			res *= self
		return res

	def div(self, num):
		# Devuelve el 'Num' dividido entre el otro 'Num'.
		# Es un algoritmo súper ineficiente.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)
		if not isinstance(num, Num): raise Exception("'num' no es de un tipo valido.")

		max_length = max(self.max_length, num.max_length)
		base = self.base

		if self.base != num.base:
			num = Num(num.value, base, max_length)

		if num.value == 0:
			raise Exception("División por 0")
		
		cont = 0
		while (num * cont).value <= self.value:
			cont += 1
		cont -= 1
		return Num(cont, base, max_length), self - (num * cont)

	def rshift(self, i):
		# Mueve todos los dígitos a la derecha i campos.
		if not isinstance(i, int): raise Exception("'i' debe ser un 'int'.")

		new = Num.copy(self)
		new._value = new._value[:-i]
		new._value = [0]*i + new._value
		return new
	
	def lshift(self, i):
		# Mueve todos los dígitos a la izquierda i campos.
		if not isinstance(i, int): raise Exception("'i' debe ser un 'int'.")

		new = Num.copy(self)
		new._value = new._value[i:]
		new._value = new._value + [0]*i
		return new


	# Operadores sobrecargados.
	def __str__(self):
		# Cuando se convierte el objeto a un 'str'.
		# Es lo que se imprime cuando uno hace print('objeto').
		return f"Num({Num.list_to_string(self._value)})[{self.base}]"

	def __repr__(self):
		# Es una representación imprimible del objeto.
		return self.__str__()

	def __int__(self):
		# Convierte el objeto a 'int' base 10.
		return self.value

	def __index__(self):
		# Convierte el objeto a 'int' base 10.
		# Se usa en slices, entre otros.
		return self.value

	def __len__(self):
		# Se utiliza cuando se hace len(Num)
		return self.max_length

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

	def __eq__(self, num):
		# Operador '=='.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)
		if not isinstance(num, Num): raise Exception("'num' no es de un tipo valido.")

		max_length = max(self.max_length, num.max_length)
		base = self.base

		if self.base != num.base:
			num = Num(num.value, base, max_length)
		
		if int(self) == int(num): return True
		return False

	def __ne__(self, num):
		# Operador '!='.
		return not self == num
	
	def __lt__(self, num):
		# Operador '<'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)
		if not isinstance(num, Num): raise Exception("'num' no es de un tipo valido.")

		max_length = max(self.max_length, num.max_length)
		base = self.base

		if self.base != num.base:
			num = Num(num.value, base, max_length)
		
		if int(self) < int(num): return True
		return False

	def __gt__(self, num):
		# Operador '>'.
		if isinstance(num, int) or isinstance(num, str) or isinstance(num, list):
			num = Num(num, self.base, self.max_length)
		if not isinstance(num, Num): raise Exception("'num' no es de un tipo valido.")

		max_length = max(self.max_length, num.max_length)
		base = self.base

		if self.base != num.base:
			num = Num(num.value, base, max_length)
		
		if int(self) > int(num): return True
		return False

	def __le__(self, num):
		# Operador '<='.
		return not self > num

	def __ge__(self, num):
		# Operador '>='.
		return not self < num
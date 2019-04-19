class Num:
	# constants
	DEFAULT_BASE = 10
	DEFAULT_LENGHT = 16
	CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyz'.upper()

	# constructor
	def __init__(self, value, base = DEFAULT_BASE, lenght = DEFAULT_LENGHT):
		self.base = base
		self.max_lenght = lenght
		if isinstance(value, list):
			current_lenght = len(value)
			if self.max_lenght < current_lenght:
				raise Exception('The value is too big')
			self.value = [0 for i in range(self.max_lenght - current_lenght)] + [int(x) for x in value]
		else:
			current_lenght = len(str(value))
			if self.max_lenght < current_lenght:
				raise Exception('The value is too big')
			if isinstance(value, int):
				self.value = [0 for i in range(self.max_lenght - current_lenght)] + [int(x) for x in str(value)]
			else:
				self.value = [0 for i in range(self.max_lenght - current_lenght)] + [int(x, base) for x in str(value)]
	
	# information
	def getValue(self):
		return int(Num.list_to_string(self.value), self.base)

	def getSize(self):
		return len(Num.list_to_string(self.value))

	# static methods
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
	
	# Operations
	def add(self, num):
		if not isinstance(num, Num):
			raise Exception("'num' is not a Num.")
		if self.max_lenght != num.max_lenght:
			raise Exception("The max lenght of the two of them is different.")
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
		return Num(new, self.base, self.max_lenght)

	def sub(self, num):
		if not isinstance(num, Num):
			raise Exception("'num' is not a Num.")
		if self.max_lenght != num.max_lenght:
			raise Exception("The max lenght of the two of them is different.")
		if self.base != num.base:
			raise Exception("The base of the two of them is different.")
		aux = self + ~num
		if(self.getValue() < num.getValue()):
			aux = ~aux
		aux = aux.value[aux.getSize() - self.getSize():]
		return Num(aux, self.base, self.max_lenght)

	# Operators
	def __add__(self, num):
		return self.add(num)

	def __invert__(self):
		return self.invert()

	def __sub__(self, num):
		return self.sub(num)

	def __str__(self):
		return f"Num({Num.list_to_string(self.value)})[{self.base}]"

if __name__ == "__main__":
	n1 = Num('10', 8)
	n2 = Num('17', 8)
	res1 = n1 + n2
	res2 = n1 - n2
	print(f"{n1} + {n2} = {res1} : default = {n1.getValue() + n2.getValue()}")
	print(f"{n1} - {n2} = {res2} : default = {n1.getValue() - n2.getValue()}")

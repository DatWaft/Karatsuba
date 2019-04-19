class Num:
	# constants
	DEFAULT_BASE = 10
	DEFAULT_LENGHT = 16

	# constructor
	def __init__(self, value, base = DEFAULT_BASE, lenght = DEFAULT_LENGHT):
		self.base = base
		self.max_lenght = lenght
		current_lenght = len(str(value))
		if self.max_lenght < current_lenght:
			raise Exception('The value is too big')

		self.value = [0 for i in range(self.max_lenght - current_lenght)] + [int(x) for x in str(value)]
	
	def getValue(self):
		return Num.list_to_string(self.value)

	# static methods
	@staticmethod
	def list_to_string(a):
		s = ''
		flag = False
		for i in a:
			if not flag and i != 0:
				flag = True
				s += str(i)
			elif flag:
				s += str(i)
		return s

	# Operations
	def add(self, num):
		if self.max_lenght != num.max_lenght:
			raise Exception("The max lenght of the two of them is different.")
		if self.base != num.base:
			raise Exception("The base of the two of them is different.")
		base = self.base
		q = []
		r = 0
		for i,j in zip(self.value[::-1], num.value[::-1]):
			q = [(i + j) % base + r] + q
			r = (i + j) // base

		return Num(Num.list_to_string(q), base)

	# Operators
	def __add__(self, num):
		return self.add(num)

	def __str__(self):
		return f"Num({Num.list_to_string(self.value)})[{self.base}]"

if __name__ == "__main__":
	n1 = Num(99)
	n2 = Num(99)
	print(f"{n1} + {n2} = {n1 + n2} : default = {int(n1.getValue()) + int(n2.getValue())}")


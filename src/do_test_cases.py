from read_test_cases import test

def do_tests():
	print("*** Doing test cases for multiplication ***")
	test('../test/test_mult.csv', '*')
	print("*** Finished test cases for multiplication ***")
	input()
	print("*** Doing test cases for addition ***")
	test('../test/test_sum.csv', '+')
	print("*** Finished test cases for addition ***")
	input()
	print("*** Doing test cases for substraction ***")
	test('../test/test_rest.csv', '-')
	print("*** Finished test cases for substraction ***")
	input()
	print("*** Doing test cases for divison ***")
	test('../test/test_div.csv', '/')
	print("*** Finished test cases for divison ***")
	input()

if __name__ == "__main__":
	do_tests()
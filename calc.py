class Calculator:
	"""Performs the four basic mathematical operations

	Methods: 
		add(number, number)
		subtract(number, number)
		multiply(number, number)
		divide(number, number)
	"""
	# def __init__(self, name):
	# 	self.name = name

	def add(self, firstOperand, secondOperand):
		"""Adds two numbers together

		Arguments:
			firstOperand -> Anynumber
			secondOperand -> an number
		"""

		return firstOperand + secondOperand

	def subtract(self, firstOperand, secondOperand):

		return firstOperand - secondOperand


	def multiply(self, firstOperand, secondOperand):

		return firstOperand * secondOperand

	def divide(self, firstOperand, secondOperand):

		return firstOperand / secondOperand

calc = Calculator()
print(dir(calc))
print(calc.add(23478945, 436080234))
calc.subtract(12536, 80954783)
calc.multiply(312580, 809)
calc.divide(134256, 7980)
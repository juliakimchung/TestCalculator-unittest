import unittest
from calc import*

def setUpModule():
	print("set up module")

def tearDownModule():
	print('tear down module')

class TestCalculator(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		print("Set Up Class")
		self.calc = Calculator()

	@classmethod
	def tearDownClass(self):
		print('Tear down class')

	def test_add(self):
		self.assertEqual(self.calc.add(35, 65), 100)
		self.assertEqual(self.calc.subtract(94, 54), 40)
		self.assertEqual(self.calc.multiply(12, 10), 120)
		self.assertEqual(self.calc.divide(100, 5), 20)



if __name__ == '__main__':
	unittest.main()






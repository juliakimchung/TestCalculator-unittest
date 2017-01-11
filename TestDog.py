import unittest
from dogs import*

def setUpModule():
	print("set up module for TestDog.py")

def tearDownModule():
	print("tear up module for TestDog.py")

class testDog(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		print("set up class for testDog class")
		self.dog = Dog("popcorn")

	@classmethod
	def tearDownClass(self):
		print("tear down class for test_dog class")

	def test_DogMustHaveNameProperty(self):
		self.dog = Dog("popcorn") 
		self.assertEqual(self.dog.name, "popcorn")

	def test_DogMustHaveSpeciesProperty(self):
		self.dog = Dog("species")
		self.assertEqual(self.dog.species, "Dog")

	def test_set_legs_method(self):
		self.dog.set_legs(4)
		self.assertEqual(self.dog.legs, 4)
	def test_DogSpeed(self):
		self.dog.legs = 4
		self.dog.walk()
		self.assertEqual(self.dog.speed, 0.8)

if __name__  ==  '__main__':
	unittest.main()
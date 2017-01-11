import unittest
from animals import*

def setUpModule():
	print("set up module for animal.py")

def tearDownModule():
	print("tear down module for animal.py")


class testAnimal(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		print("set up class for testAnimal class")
		self.animal = Animal("Happy", "Dog")
	@classmethod
	def tearDownClass(self):
		print("tear down class")


 	
	def test_AnimalMustHaveNameProperty(self):

		self.animal = Animal("Happy","Dog")
		self.assertEqual(self.animal.name, "Happy")

	def test_AnimalMustHaveSpecies(self):
		self.animal = Animal("Happy","Dog")
		self.assertEqual(self.animal.species, "Dog")

	def test_get_name_method(self):
		self.animal.name = "Happy"
		self.assertEqual(self.animal.get_name(), "Happy")
	def test_set_legs_method(self):
		self.animal.set_legs(4)
		self.assertEqual(self.animal.legs , 4)
	def test_set_species_method(self):
		self.animal.set_species("Arachnid")
		self.assertEqual(self.animal.species, "Arachnid")
	def test_AnimalSpeed(self):
		self.animal.legs = 4
		self.animal.walk()
		self.assertEqual(self.animal.speed, 0.4) 



if __name__ == '__main__':
		unittest.main()
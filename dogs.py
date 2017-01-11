from animals import*
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
        # self.name = name
        # self.species = "Dog"

    def walk(self):
        """Sets the speed of the dog"""
        self.speed = self.speed + (0.2 * self.legs)


# dog = Dog("Ray")
# dog.legs = 4
# dog.walk()
# print(dog.speed)
# print(dog)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def get_name(self):
        """Returns the animal's name"""
        
        return self.name

    def walk(self):
        """Sets the speed of the animal"""
        if isinstance(self.legs, int) and self.legs > 0:
            self.speed = self.speed + (0.1 * self.legs)
        else:
            raise ValueError('Legs property must contain a number greater than 0')

    def set_legs(self, number_of_legs):
        """Sets the species of the animal"""
        self.legs = number_of_legs

    def set_species(self, species):
        """Sets the species of the animal"""
        self.species = species

    def get_species(self):
        """Returns the species of the animal"""
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)
    
# animal = Animal("happy", "parrot")
# print(dir(animal))
# print(animal.get_name())
# print(animal)
# print(animal.walk(4))
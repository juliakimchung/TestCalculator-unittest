from animals import*
from dogs import*
animal = Animal("happy", "parrot")
animal.legs = 4
animal.walk()
print(animal.speed)

print(dir(animal))
print(animal.get_name())
print(animal)
dog = Dog("Ray")
dog.legs = 4
dog.walk()
print(dog.speed)
print(dog)
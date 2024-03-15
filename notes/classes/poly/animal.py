class Creature:
    def __init__(self, creature_type):
        self.__creature_type = creature_type

    def __str__(self):
        return self.__creature_type


class Mammal(Creature):  # Inherit from Creature (polymorphism
    def __init__(self, species):
        Creature.__init__(self, "Mammal")
        self.__species = species

    def show_species(self):
        print("I am a", self.__species)

    def make_sound(self):
        print("Grrr")


class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Dog")  # Call super class constructor

    def make_sound(self):  # Override super class method (polymorphism)
        print("Woof! Woof!")


class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Cat")  # Call super class constructor

    def make_sound(self):  # Override super class method (polymorphism)
        print("Meow")

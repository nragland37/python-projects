class Creature:
    def __init__(self, creature_type):
        self.__creature_type = creature_type

    def __str__(self):
        return self.__creature_type


# Inherit from Creature class (super class)
class Mammal(Creature):
    def __init__(self, species):
        Creature.__init__(self, "Mammal")
        self.__species = species

    def show_species(self):
        print("I am a", self.__species)

    def make_sound(self):
        print("Grrr")


class Dog(Mammal):
    def __init__(self):
        # Call super class constructor
        Mammal.__init__(self, "Dog")

    # Override super class method (polymorphism)
    def make_sound(self):
        print("Woof! Woof!")


class Cat(Mammal):
    def __init__(self):
        # Call super class constructor
        Mammal.__init__(self, "Cat")

    # Override super class method (polymorphism)
    def make_sound(self):
        print("Meow")

from animal import Creature, Mammal, Dog, Cat


def show_mammal_info(obj):
    if isinstance(obj, Mammal):  # Check if obj is a Mammal
        obj.make_sound()
        obj.show_species()
    else:
        print("Here is not a Mammal")
    
def main():
    mammal = Mammal('generic Mammal')
    myDog = Dog()
    myCat = Cat()
    
    show_mammal_info(mammal)
    show_mammal_info(myDog)
    show_mammal_info(myCat)
    
    creature_obj = Creature('generic creature')
    show_mammal_info(creature_obj)
    
    # mammal.show_species()
    # mammal.make_sound()
    
    # myDog.show_species()
    # myDog.make_sound()
    
    # myCat.show_species()
    # myCat.make_sound()
    
    # print(myCat)
    
if __name__ == '__main__':
    main()
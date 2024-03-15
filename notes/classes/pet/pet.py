class Pet:
    def __init__(self, pet_type, name):  # constructor
        self.__pet_type = pet_type
        self.__name = name

    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # it will convert the object to a string
    def __str__(self):
        return f"{self.__name} : {self.__pet_type}"

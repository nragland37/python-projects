# ****************************************************************************************************
#
#       This file defines the Person class which is a parent class of Customer and SalesAssociate.
#
# ****************************************************************************************************


class Person:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone


# ****************************************************************************************************

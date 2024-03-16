# ****************************************************************************************************
#
#       This file defines the Customer class which is a child class of Person.
#
#       Other files required:
#         1.    person.py - defines the Person class (parent class of Customer)
#
# ****************************************************************************************************

from person import Person


class Customer(Person):
    def __init__(self, name, phone, customer_number, mailing_list):
        Person.__init__(self, name, phone)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def get_mailing_list(self):
        return self.__mailing_list

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def __str__(self):
        return (
            f"{self.get_name():10}"
            f"{self.get_phone():10}"
            f"{self.__customer_number:10}"
            f'{"Yes" if self.__mailing_list else "No"}'
        )


# ****************************************************************************************************

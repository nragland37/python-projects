# ****************************************************************************************************
#
#       This file defines the SalesAssociate class which is a child class of Person.
#
#       Other files required:
# 		  1.    person.py - defines the Person class (parent class of SalesAssociate)
#
# ****************************************************************************************************

from person import Person

# ****************************************************************************************************


class SalesAssociate(Person):
    def __init__(self, name, phone, sales_id, commission):
        Person.__init__(self, name, phone)
        self.__sales_id = sales_id
        self.__commission = commission

    # ****************************************************************************************************

    def get_sales_id(self):
        return self.__sales_id

    # ****************************************************************************************************

    def set_sales_id(self, sales_id):
        self.__sales_id = sales_id

    # ****************************************************************************************************

    def get_commission(self):
        return self.__commission

    # ****************************************************************************************************

    def set_commission(self, commission):
        self.__commission = commission

    # ****************************************************************************************************

    def __str__(self):
        return (
            f"{self.get_name():10}"
            f"{self.get_phone():10}"
            f"{self.__sales_id:10}"
            f"{self.__commission:,.2f}"
        )


# ****************************************************************************************************

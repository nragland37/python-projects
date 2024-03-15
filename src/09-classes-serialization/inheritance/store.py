# ****************************************************************************************************
#
#       This program demonstrates the use of classes and inheritance by creating dictionaries to
#       store sales associates and customers.
#
#       Other files required:
# 		  1.    customer.py - defines the Customer class (child class of Person)
# 		  2.    sales_associate.py - defines the SalesAssociate class (child class of Person)
# 		  3.    person.py - defines the Person class (parent class of Customer and SalesAssociate)
#
# ****************************************************************************************************

from customer import Customer
from sales_associate import SalesAssociate

# ****************************************************************************************************


def display_sales(associates_dict):
    print(f'\n\n{"All Sales":^50}')
    print(f'\n{"Name":10}{"Phone":10}{"ID":10}{"Commission"}')
    print(f'{"-" * 50}')

    for associate in associates_dict.values():
        print(associate)
    print(f'{"-" * 50}')


# ****************************************************************************************************


def display_customers(customers_dict):
    print(f'\n\n{"All Customers":^50}')
    print(f'\n{"Name":10}{"Phone":10}{"Cust#":10}{"Mailing List"}')
    print(f'{"-" * 50}')

    for customers_list in customers_dict.values():
        for customer in customers_list:
            print(customer)
    print(f'{"-" * 50}')


# ****************************************************************************************************


def display_sales_customers(associates_dict, customers_dict):
    print(f'\n\n{"Sales Associates and Customers":^50}')
    print(f'\n{"Sales":20}{"Customers"}')
    print(f'{"-" * 50}')

    for k, v in associates_dict.items():
        customers_list = customers_dict.get(k, [])

        if customers_list:
            print(f"{v.get_name():20}", end="")

            for customer in customers_list:
                print(customer.get_name(), end=", ")
            print()
        else:
            print(f"{v.get_name():20}{'N/A'}")
    print(f'{"-" * 50}')


# ****************************************************************************************************


def main():
    associates_dict = {
        "A905": SalesAssociate("Jane", "123-987", "A905", 8.7),
        "X337": SalesAssociate("John", "905-437", "X337", 9.5),
        "B522": SalesAssociate("Joe", "314-636", "B522", 10.7),
        "Y777": SalesAssociate("Jill", "112-616", "Y777", 0),
        "Z123": SalesAssociate("Jack", "897-909", "Z123", 101010.10),
    }

    customers_dict = {
        "A905": [
            Customer("Mary", "909-457", "C921", True),
            Customer("Hairy", "313-436", "C123", False),
        ],
        "X337": [
            Customer("Mike", "415-678", "C100", False),
            Customer("Ike", "314-636", "C200", True),
            Customer("Candy", "112-616", "C300", False),
        ],
        "B522": [
            Customer("Moe", "897-909", "C607", True),
            Customer("Curly", "311-444", "C800", False),
            Customer("Larry", "304-666", "C900", False),
        ],
        "Z123": [
            Customer("Obi-Wan", "909-457", "C921", True),
            Customer("Anakin", "313-436", "C123", False),
            Customer("Yoda", "415-678", "C100", False),
            Customer("Luke", "314-636", "C200", True),
        ],
    }

    display_sales(associates_dict)
    display_customers(customers_dict)
    display_sales_customers(associates_dict, customers_dict)


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************
"""

                    All Sales                     

Name      Phone     ID        Commission
--------------------------------------------------
Jane      123-987   A905      8.70
John      905-437   X337      9.50
Joe       314-636   B522      10.70
Jill      112-616   Y777      0.00
Jack      897-909   Z123      101,010.10
--------------------------------------------------


                  All Customers                   

Name      Phone     Cust#     Mailing List
--------------------------------------------------
Mary      909-457   C921      Yes
Hairy     313-436   C123      No
Mike      415-678   C100      No
Ike       314-636   C200      Yes
Candy     112-616   C300      No
Moe       897-909   C607      Yes
Curly     311-444   C800      No
Larry     304-666   C900      No
Obi-Wan   909-457   C921      Yes
Anakin    313-436   C123      No
Yoda      415-678   C100      No
Luke      314-636   C200      Yes
--------------------------------------------------


          Sales Associates and Customers          

Sales               Customers
--------------------------------------------------
Jane                Mary, Hairy, 
John                Mike, Ike, Candy, 
Joe                 Moe, Curly, Larry, 
Jill                N/A
Jack                Obi-Wan, Anakin, Yoda, Luke, 
--------------------------------------------------

"""

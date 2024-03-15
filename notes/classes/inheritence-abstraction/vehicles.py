class Automobile:
    def __init__(self, make, price):
        self._make = make
        self._price = price

    def set_make(self, make):
        self._make = make

    def get_make(self):
        return self._make

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price


# abstract class is a class that is not meant to be instantiated
# it is meant to be inherited from and used as a base class
# therefore it does not need a __str__ method
# because it is not meant to be instantiated and printed


class Car(Automobile):
    def __init__(self, make, price, doors):
        # super() is a reference to the parent class
        super().__init__(make, price)
        # Automobile.__init__(self, make, price)
        # but super() will automatically reference the parent class
        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors

    def __str__(self):
        return (
            f"Make: {self._make}\n" f"Price: {self._price}\n" f"Doors: {self.__doors}\n"
        )


class Truck(Automobile):
    def __init__(self, make, price, drive_type):
        super().__init__(make, price)
        self.__drive_type = drive_type

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type

    def __str__(self):
        return (
            f"Make: {self._make}\n"
            f"Price: {self._price}\n"
            f"Drive Type: {self.__drive_type}\n"
        )

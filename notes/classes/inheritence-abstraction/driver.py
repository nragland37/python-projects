from vehicles import Car, Truck

# Notice, Automobile is not imported because it is not meant to be instantiated
# it is meant to be inherited from and used as a base/abstract class
# This is an example of data abstraction (hiding the details of the implementation)


def main():
    myCar = Car("Toyota", 20000, 4)
    myTruck = Truck("Ford", 25000, "4WD")

    print(myCar)
    print(myTruck)


if __name__ == "__main__":
    main()

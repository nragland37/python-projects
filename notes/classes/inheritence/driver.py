from vehicles import Automobile, Car, Truck


def main():
    myCar = Car("Toyota", 20000, 4)
    myTruck = Truck("Ford", 25000, "4WD")

    print(myCar)
    print(myTruck)


if __name__ == "__main__":
    main()

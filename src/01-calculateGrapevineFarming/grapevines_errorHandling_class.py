# ****************************************************************************************************
#
#       This program updates the grapevines_errorHandling.py program to include a Vineyard class.
#
# ****************************************************************************************************


class Vineyard:
    COEFFICIENT = 2

    def __init__(self):
        self.row = 0.0
        self.amount = 0.0
        self.space = 0.0

    # ************************************************************************************************

    def get_input(self, prompt):
        while True:
            try:
                val = float(input(prompt))
                if val < 0:
                    raise ValueError
                return val
            except ValueError:
                print("\nError: cannot be negative and must be a number.\n")

    # ************************************************************************************************

    def get_vines(self):
        try:
            return (self.row - self.COEFFICIENT * self.amount) / self.space
        except ZeroDivisionError:
            print("\nError: cannot divide by zero.\n")
            return None

    # ************************************************************************************************

    def get_choice(self):
        while True:
            ch = input("\nWould you like to run the program again? (y/n): ").lower()
            if ch in ["y", "n"]:
                return ch
            print('\nError: must be "y" or "n".')

    # ************************************************************************************************

    def main(self):
        self.row = self.get_input("Enter the row length (in feet): ")
        self.amount = self.get_input(
            "Enter space used by an end-post assembly (in feet): "
        )
        self.space = self.get_input("Enter the distance between each vine (in feet): ")

        vines = self.get_vines()

        if vines is not None:
            if vines > 0:
                print(f"You have enough space for {vines} vines.")
            else:
                print("You do not have enough space for any vines.")

    # ************************************************************************************************

    def run(self):
        while True:
            self.main()
            if self.get_choice() == "n":
                print("\nGoodbye!")
                break


# ****************************************************************************************************


def main():
    vineyard = Vineyard()
    vineyard.run()


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************

#   Enter the row length (in feet): 300
#   Enter space used by an end-post assembly (in feet): 1.5
#   Enter the distance between each vine (in feet): 2.2
#   You have enough space for 135.0 vines.

#   Would you like to run the program again? (y/n): n

#   Goodbye!

# ****************************************************************************************************

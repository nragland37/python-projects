# ****************************************************************************************************
#
#       This program updates the grapevines.py program to include error handling and a loop to
#       allow the user to run the program multiple times.
#
# ****************************************************************************************************

COEFFICIENT = 2

# ****************************************************************************************************


def get_input(prompt):
    while True:
        try:
            val = float(input(prompt))

            if val < 0:
                raise ValueError
            return val

        except ValueError:
            print("\nError: cannot be negative and must be a number.\n")


# ****************************************************************************************************


def get_vines(row, amount, space):
    try:
        return (row - COEFFICIENT * amount) / space
    except ZeroDivisionError:
        print("\nError: cannot divide by zero.\n")
        return None


# ****************************************************************************************************


def get_choice():
    while True:
        ch = input("\nWould you like to run the program again? (y/n): ").lower()

        if ch in ["y", "n"]:
            return ch
        print('\nError: must be "y" or "n".')


# ****************************************************************************************************


def main():
    row = get_input("Enter the row length (in feet): ")
    amount = get_input("Enter space used by an end-post assembly (in feet): ")
    space = get_input("Enter the distance between each vine (in feet): ")

    vines = get_vines(row, amount, space)

    if vines is not None:
        if vines > 0:
            print(f"You have enough space for {vines} vines.")
        else:
            print("You do not have enough space for any vines.")


# ****************************************************************************************************

if __name__ == "__main__":
    while True:
        main()

        if get_choice() == "n":
            print("\nGoodbye!")
            break

# ****************************************************************************************************
#
#   Enter the row length (in feet): 300
#   Enter space used by an end-post assembly (in feet): 1.5
#   Enter the distance between each vine (in feet): 2.2
#   You have enough space for 135.0 vines.
#
#   Would you like to run the program again? (y/n): n
#
#   Goodbye!
#
#
# ****************************************************************************************************

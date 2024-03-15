# ****************************************************************************************************
#
#       This program calculates the number of grapevines that can be planted in a vineyard row
#       based on the amount of space used.
#
# ****************************************************************************************************

COEFFICIENT = 2

# ****************************************************************************************************


def get_vines(row, amount, space):
    return (row - COEFFICIENT * amount) / space


# ****************************************************************************************************


def main():
    row = float(input("Enter the length of the row, in feet: "))
    amount = float(
        input("Enter the amount of space, in feet, used by an end-post assembly: ")
    )
    space = float(input("Enter the distance, in feet, between each vine: "))

    vines = get_vines(row, amount, space)
    print(f"You have enough space for {vines} vines.")


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************

# Enter the length of the row, in feet: 300
# Enter the amount of space, in feet, used by an end-post assembly: 1.5
# Enter the distance, in feet, between each vine: 2.2
# You have enough space for 135.0 vines.

# *****************************************************************************************************

# Enter the length of the row, in feet: 100
# Enter the amount of space, in feet, used by an end-post assembly: 5
# Enter the distance, in feet, between each vine: 2
# You have enough space for 45.0 vines.

# *****************************************************************************************************

# ****************************************************************************************************
#
#       This program prompts the user to enter values for a 3x3 square and checks if it is a Lo
#       Shu Magic Square. A Lo Shu Magic Square is a 3x3 grid that contains the numbers 1-9 such
#       that the sum of the numbers in each row, each column, and each of the two main diagonals
#       is the same.
#       Example: loShu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
#       The sum of each row, column, and main diagonal is 15.
#
# ****************************************************************************************************


def get_input(square):
    print("Enter all values: ")

    for row in range(len(square)):
        print(f'\n{"Row " + str(row):^11}\n{"-" * 11}')

        for col in range(len(square[row])):
            success = False

            while not success:
                try:
                    val = int(input("enter: "))

                    if 1 <= val <= 9:
                        square[row][col] = val
                        success = True
                        # if val not in square[row]:
                        #     square[row][col] = val
                        #     success = True
                        # else:
                        #     raise ValueError('Value already exists in row.')
                    else:
                        raise ValueError("Value must be between 1 and 9.")
                except ValueError as e:
                    print(f"\nError: {e}\n")

    return square


# ****************************************************************************************************


def check_left_diagnol(square):
    return sum([square[i][i] for i in range(len(square))]) == 15


# ****************************************************************************************************


def check_right_diagnol(square):
    return sum([square[i][2 - i] for i in range(len(square))]) == 15


# ****************************************************************************************************


def check_rows(square):
    return all([sum(row) == 15 for row in square])


# ****************************************************************************************************


def check_cols(square):
    return all([sum(row[col] for row in square) == 15 for col in range(len(square[0]))])


# ****************************************************************************************************


def check_lo_shu(square):
    checks = [
        check_left_diagnol(square),
        check_right_diagnol(square),
        check_rows(square),
        check_cols(square),
    ]

    return all(checks)


def is_lo_shu(square):
    success = True

    if sum([square[i][i] for i in range(len(square))]) != 15:
        success = False
    elif sum([square[i][2 - i] for i in range(len(square))]) != 15:
        success = False
    elif not all([sum(row) == 15 for row in square]):
        success = False
    elif not all(
        [sum(row[col] for row in square) == 15 for col in range(len(square[0]))]
    ):
        success = False

    return success


# ****************************************************************************************************


def display(square):
    print(f'\n{"Square:":^11}\n{"-" * 11}')

    for row in square:
        for col in row:
            print(f"{col:<5}", end="")
        print()


# ****************************************************************************************************


def main():
    square = [[0] * 3 for _ in range(3)]
    square = get_input(square)
    display(square)

    if check_lo_shu(square):
        print("\nThis is a Lo Shu Magic Square.")
    else:
        print("\nThis is not a Lo Shu Magic Square.")


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************
"""

Enter all values: 

   Row 0   
-----------
enter: 4
enter: 9
enter: 2

   Row 1   
-----------
enter: 3
enter: 5
enter: 7

   Row 2   
-----------
enter: 8
enter: 1
enter: 6

  Square:  
-----------
4    9    2    
3    5    7    
8    1    6    

This is a Lo Shu Magic Square.

****************************************************************************************************

Enter all values: 

   Row 0   
-----------
enter: 1
enter: 2
enter: 3

   Row 1   
-----------
enter: 1
enter: 2
enter: 3

   Row 2   
-----------
enter: 1
enter: 2
enter: 3

  Square:  
-----------
1    2    3    
1    2    3    
1    2    3    

This is not a Lo Shu Magic Square.

"""
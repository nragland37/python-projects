# ****************************************************************************************************
#
#       This program will generate two random numbers and quiz the user on the sum of the two
#       numbers while handling errors and allowing the user to run the program multiple times.
#
# ****************************************************************************************************

import random as r

# ****************************************************************************************************


def get_randNums(RAND_RANGE):
    # * unpacks the tuple or list and passes each element as an argument
    return r.randint(*RAND_RANGE), r.randint(*RAND_RANGE)


# ****************************************************************************************************


def get_sum(num1, num2):
    return num1 + num2


# ****************************************************************************************************


def get_choice():
    while True:
        ch = input("Again? press Y/y to continue ").lower()

        if ch in ("y", "n"):
            break

        print("\nInvalid: Must be Y/y or N/n")

    return ch


# ****************************************************************************************************


def get_input(num1, num2, MIN_SUM, MAX_SUM):
    while True:
        print(f"{'=' * 50}\n{num1:5}\n+{num2:4}")

        try:
            guess = int(input("Enter sum of numbers: "))

            if (guess < MIN_SUM) or (guess > MAX_SUM):
                raise ValueError(
                    f"Invalid: Must be an integer between {MIN_SUM} and {MAX_SUM}"
                )

            return guess

        except ValueError as e:
            print(f"\n{e}")


# ****************************************************************************************************


def display_result(guess, sum):
    if guess == sum:
        print("\nCorrect answer - Good Work!")
    else:
        print(f"\nIncorrect... The correct answer is: {sum}.")


# ****************************************************************************************************


def main():
    RAND_RANGE = (0, 999)
    MIN_SUM = 0
    MAX_SUM = RAND_RANGE[1] * 2

    while True:
        num1, num2 = get_randNums(RAND_RANGE)
        sum = get_sum(num1, num2)
        guess = get_input(num1, num2, MIN_SUM, MAX_SUM)
        display_result(guess, sum)

        if get_choice() == "n":
            break


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************

# ==================================================
#   253
# + 824
# Enter sum of numbers: 500

# Incorrect... The correct answer is: 1077.
# Again? press Y/y to continue y
# ==================================================
#   852
# + 731
# Enter sum of numbers: 1583

# Correct answer - Good Work!
# Again? press Y/y to continue n


# ****************************************************************************************************


# ==================================================
#   186
# + 856
# Enter sum of numbers: a

# invalid literal for int() with base 10: 'a'
# ==================================================
#   186
# + 856
# Enter sum of numbers: -100

# Invalid: Must be an integer between 0 and 1998
# ==================================================
#   186
# + 856
# Enter sum of numbers: /

# invalid literal for int() with base 10: '/'
# ==================================================
#   186
# + 856
# Enter sum of numbers: 1

# Incorrect... The correct answer is: 1042.
# Again? press Y/y to continue n

# ****************************************************************************************************
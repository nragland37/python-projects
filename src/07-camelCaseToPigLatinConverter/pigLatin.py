# ****************************************************************************************************
#
#       This program prompts the user to enter a string in upper camel case and converts it to
#       normal case and pig latin.
#
# ****************************************************************************************************


def pig_latin(user_string):
    words = user_string.upper().split()
    translate = [word[1:] + word[0] + "AY" for word in words]

    return " ".join(translate)


def convert(user_string):
    norm = user_string[0]

    for ch in user_string[1:]:
        if ch.isupper():
            norm += " " + ch.lower()
        else:
            norm += ch

    return norm


def main():
    user_string = input("Enter a string: ")

    norm_string = convert(user_string)
    pig_lantin_string = pig_latin(norm_string)

    print(f"\nNormal string is: {norm_string}")
    print(f"Pig Latin is: {pig_lantin_string}")


if __name__ == "__main__":
    main()

# ****************************************************************************************************

# Enter a string: StopAndSmellTheRoses

# Normal string is: Stop and smell the roses
# Pig Latin is: TOPSAY NDAAY MELLSAY HETAY OSESRAY

# *****************************************************************************************************

# Enter a string: ISleptMostOfTheNight

# Normal string is: I slept most of the night
# Pig Latin is: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

# *****************************************************************************************************

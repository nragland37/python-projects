# ****************************************************************************************************
#
#       This program...
#
#       Other files required:
# 		  1.    example.txt - contains example data
# 		  2.    example.py - defines the Example class
#
# ****************************************************************************************************


def main():
    # open the file for reading and close it automatically
    with open("example.txt", "r") as file:
        # read the entire file and split each line into a list
        data = file.read().splitlines()


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************

# attach sample output here.

# ****************************************************************************************************

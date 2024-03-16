# ****************************************************************************************************
#
#       This program updates the champions.py program by not using a list to store the World Series
#       winners. Instead, it passes the file object to functions directly and resets the file pointer
#       to the beginning of the file after each menu choice. This demonstrates how to use file
#       objects to read and write data without using lists.
#
#       Other files required:
# 		  1.    WorldSeriesWinners.txt - contains world series winners (1903-2009)
#
# ****************************************************************************************************


def searchTeam(teams, team_name):
    try:
        wins = 0
        for line in teams:
            if line.strip() == team_name:
                wins += 1

        if wins == 0:
            print(f"The {team_name} never won the World Series.")
        else:
            print(f"The {team_name} won {wins} times between 1903 and 2008.")

    except Exception as e:
        print("An error occurred: ", e)


def display(teams):
    try:
        year = 1903
        print("\nWorld Series Winners 1903-2008")

        for line in teams:
            print(f"{year}: ", end="")

            if year == 1904 or year == 1994:
                print("No World Series this year.")
            else:
                print(line, end="")

            year += 1

        print()
    except Exception as e:
        print("An error occurred: ", e)


def menu(teams):
    choice = 0

    while choice != 3:
        teams.seek(0)
        try:
            print("MENU\n1. Search a team\n2. Display team names\n3. Quit")
            choice = int(input("\nEnter the number of your choice: "))
        except ValueError:
            print("Please enter an integer.\n")
        except Exception as e:
            print("An error occurred: ", e)
        else:
            if choice == 1:
                team_name = input("\nEnter the MLB team name: ").title()
                searchTeam(teams, team_name)
            elif choice == 2:
                display(teams)
            elif choice == 3:
                print("Goodbye!")
            else:
                print("There was an indexing error. Try again.\n")
        finally:
            print("=" * 60)


def main():
    try:
        with open("WorldSeriesWinners.txt", "r") as teams:
            menu(teams)
    except FileNotFoundError:
        print("File could not be found.")


if __name__ == "__main__":
    main()

# ****************************************************************************************************

#                       Menu
# ==================================================
# 1. Search a team
# 2. Display team names
# 3. Quit
# Enter your choice: 2

#    World Series Champions between 1903 and 2009
# ==================================================
#  1 : Anaheim Angels
#  2 : Arizona Diamondbacks
#  3 : Atlanta Braves
#  4 : Baltimore Orioles
#  5 : Boston Americans
#  6 : Boston Braves
#  7 : Boston Red Sox
#  8 : Brooklyn Dodgers
#  9 : Chicago Cubs
# 10 : Chicago White Sox
# 11 : Cincinnati Reds
# 12 : Cleveland Indians
# 13 : Detroit Tigers
# 14 : Florida Marlins
# 15 : Kansas City Royals
# 16 : Los Angeles Dodgers
# 17 : Milwaukee Braves
# 18 : Minnesota Twins
# 19 : New York Giants
# 20 : New York Mets
# 21 : New York Yankees
# 22 : Oakland Athletics
# 23 : Philadelphia Athletics
# 24 : Philadelphia Phillies
# 25 : Pittsburgh Pirates
# 26 : St. Louis Cardinals
# 27 : Toronto Blue Jays
# 28 : Washington Senators

#                        Menu
# ==================================================
# 1. Search a team
# 2. Display team names
# 3. Quit
# Enter your choice: 1

# Enter the name of a team: St. Louis Cardinals

# The St. Louis Cardinals won the world series 10 times between 1903 and 2009.

#                        Menu
# ==================================================
# 1. Search a team
# 2. Display team names
# 3. Quit
# Enter your choice: 1

# Enter the name of a team: ST. louis cArDiNaLS

# The St. Louis Cardinals won the world series 10 times between 1903 and 2009.

#                        Menu
# ==================================================
# 1. Search a team
# 2. Display team names
# 3. Quit
# Enter your choice: 1

# Enter the name of a team: Dataframe Pandas

# The Dataframe Pandas never won the world series.

#                        Menu
# ==================================================
# 1. Search a team
# 2. Display team names
# 3. Quit
# Enter your choice: 3

# Goodbye!

# ****************************************************************************************************

# ****************************************************************************************************
#
#       This program reads from a file containing World Series winners between 1903 and 2009 and
#       creates lists of unique teams and their counts. It prompts the user with a menu for various
#       operations on the lists.
#
#       Other files required:
# 		  1.    WorldSeriesWinners.txt - contains world series winners (1903-2009)
#
# ****************************************************************************************************


def display_teams(teams):
    print(f'\n{"World Series Champions between 1903 and 2009":^50}\n{"=" * 50}')

    for i, team in enumerate(teams, 1):
        print(f"{i:2} : {team}")


def search_team(teams_count, team_name):
    count = teams_count.count(team_name)

    if count:
        print(
            f"\nThe {team_name} won the world series {count} times between 1903 and 2009."
        )
    else:
        print(f"\nThe {team_name} never won the world series.")


def menu(teams_count, teams):
    while True:
        try:
            print(f'\n{"Menu":^50}\n{"=" * 50}')
            print("1. Search a team\n2. Display team names\n3. Quit")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                team_name = input("\nEnter the name of a team: ").strip().title()
                search_team(teams_count, team_name)
            elif ch == 2:
                display_teams(teams)
            elif ch == 3:
                print("\nGoodbye!")
                break
            else:
                raise ValueError(f"{ch} is out of range")

        except ValueError as ve:
            print(f"\nThere was an indexing error: {ve}. Try again (1-3).")
        except Exception as e:
            print(f"\nAn error occurred: {e}. Try again (1-3).")


def main():
    try:
        with open("WorldSeriesWinners.txt", "r") as file:
            teams_count = file.read().splitlines()
        teams = sorted(set(teams_count))
        menu(teams_count, teams)

    except FileNotFoundError as fnfe:
        print(f"The file could not be found: {fnfe}")
    except Exception as e:
        print(f"An error occurred: {e}")


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

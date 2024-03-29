# ****************************************************************************************************
#
#       This program updates the champions.py program to include searching by index of the teams
#       and not just by name.
#
#       Other files required:
# 		  1.    WorldSeriesWinners.txt - contains world series winners (1903-2009)
#
# ****************************************************************************************************


def displayTeams(teams):
    print(f'\n{"Teams":^30}\n{"=" * 30}')

    for i, team in enumerate(teams):
        print(f"{i:2} : {team}")


def displayCount(team, teamsCount):
    count = teamsCount.count(team)

    if count:
        print(f"\nThe {team} won the World Series {count} times between 1903 and 2009.")
    else:
        print(f"\nThe {team} never won the World Series.")


def processMenu(teamsCount, teams):
    while True:
        try:
            print(f'\n{"Menu":^30}\n{"=" * 30}')
            print(
                "1. Search a team\n2. Search a team by index\n3. Display team names\n4. Quit"
            )
            ch = int(input("Enter your choice: "))

            if ch == 1:
                teamName = input("\nEnter the name of a team: ").strip().title()
                displayCount(teamName, teamsCount)
            elif ch == 2:
                index = int(input("\nEnter the index of the team: "))
                teamIndex = teams[index]
                displayCount(teamIndex, teamsCount)
            elif ch == 3:
                displayTeams(teams)
            elif ch == 4:
                print("\nGoodbye!")
                break
            else:
                raise ValueError(f"{ch} is not in range.")

        except ValueError as ve:
            print(f"\nThere was an indexing error: {ve}")
        except IndexError:
            print("There was an indexing error for the team index.")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    try:
        with open("WorldSeriesWinners.txt", "r") as file:
            teamsCount = [line.strip() for line in file]
        teams = sorted(set(teamsCount))
        processMenu(teamsCount, teams)

    except FileNotFoundError:
        print("The file could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

# ****************************************************************************************************

#              Menu
# ==============================
# 1. Search a team
# 2. Search a team by index
# 3. Display team names
# 4. Quit
# Enter your choice: 3

#             Teams
# ==============================
#  0 : Anaheim Angels
#  1 : Arizona Diamondbacks
#  2 : Atlanta Braves
#  3 : Baltimore Orioles
#  4 : Boston Americans
#  5 : Boston Braves
#  6 : Boston Red Sox
#  7 : Brooklyn Dodgers
#  8 : Chicago Cubs
#  9 : Chicago White Sox
# 10 : Cincinnati Reds
# 11 : Cleveland Indians
# 12 : Detroit Tigers
# 13 : Florida Marlins
# 14 : Kansas City Royals
# 15 : Los Angeles Dodgers
# 16 : Milwaukee Braves
# 17 : Minnesota Twins
# 18 : New York Giants
# 19 : New York Mets
# 20 : New York Yankees
# 21 : Oakland Athletics
# 22 : Philadelphia Athletics
# 23 : Philadelphia Phillies
# 24 : Pittsburgh Pirates
# 25 : St. Louis Cardinals
# 26 : Toronto Blue Jays
# 27 : Washington Senators

#              Menu
# ==============================
# 1. Search a team
# 2. Search a team by index
# 3. Display team names
# 4. Quit
# Enter your choice: 2

# Enter the index of the team: 9

# The Chicago White Sox won the World Series 3 times between 1903 and 2009.

#              Menu
# ==============================
# 1. Search a team
# 2. Search a team by index
# 3. Display team names
# 4. Quit
# Enter your choice: 1

# Enter the name of a team: St. Louis Cardinals

# The St. Louis Cardinals won the World Series 10 times between 1903 and 2009.

#              Menu
# ==============================
# 1. Search a team
# 2. Search a team by index
# 3. Display team names
# 4. Quit
# Enter your choice: 4

# Goodbye!

# ****************************************************************************************************

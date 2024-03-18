# ****************************************************************************************************
#
#       This program reads from a file containing World Series winners between 1903 and 2009 and
#       creates a dictionary of unique teams and their winning years. It prompts the user with a
#       menu created using a dictionary for various operations on the dictionary of teams.
#
#       Other files required:
# 		  1.    WorldSeriesWinners.txt - contains world series winners (1903-2009)
#
# ****************************************************************************************************


def get_dict(teams):
    team_dict = {}
    year = "1903"

    for team in teams:
        if team != "none":
            if team in team_dict:
                team_dict[team].add(year)
            else:
                team_dict[team] = {year}
        year = str(int(year) + 1)

    return team_dict


def display_years(years):
    sorted_years = sorted(years)

    for i in range(0, len(sorted_years), 8):
        print(" ".join(sorted_years[i : i + 8]))


def display_team(team_dict):
    team_name = input("Enter a team's name: ").strip().title()

    if team_name in team_dict:
        years = team_dict[team_name]

        if years:
            print(f"\n{team_name}:")
            display_years(years)
        else:
            print(f"\n{team_name}:\nNo wins")
    else:
        print(f"\n{team_name} not found.")


def display(team_dict):
    for team, years in team_dict.items():
        print(f"\n{team}:")
        display_years(years)


def delete_team(team_dict):
    team_name = input("Enter a team's name: ").strip().title()

    if team_name in team_dict:
        del team_dict[team_name]
        print(f"\n{team_name} deleted")
    else:
        print(f"\n{team_name} not found")


def update_team(team_dict):
    team_name = input("Enter a team's name: ").strip().title()
    new_years = set(input("Enter this team's new winning year(s): ").strip().split())

    if team_name in team_dict:
        team_dict[team_name] = new_years
        print(f"\n{team_name} updated")
    else:
        print(f"\n{team_name} not found")


def menu(teams):
    MENU = {1: display_team, 2: display, 3: delete_team, 4: update_team}
    success = True
    team_dict = get_dict(teams)

    while success:
        print(f'\n{"Menu":^30}\n{"=" * 30}')
        print(
            "1. View a team's info\n"
            "2. View all team's info\n"
            "3. Delete a team's info\n"
            "4. Change a team's info\n"
            "5. Quit"
        )
        try:
            ch = int(input("Enter your choice: "))

            if ch == 5:
                print("Goodbye!")
                success = False
            else:
                MENU[ch](team_dict)

        except ValueError as ve:
            print(f"\nError: {ve}")
        except KeyError as ke:
            print(f"\nError: {ke} is not a valid choice")
        except Exception as e:
            print(f"\nError: {e}")


def main():
    try:
        with open("WorldSeriesWinners.txt", "r") as file:
            teams = file.read().splitlines()
        menu(teams)

    except FileNotFoundError as fnfe:
        print(f"\nError: {fnfe}")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()

# ****************************************************************************************************

#              Menu
# ==============================
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Enter your choice: 1
# Enter a team's name: St. Louis Cardinals

# St. Louis Cardinals:
# 1926 1931 1934 1942 1944 1946 1964 1967
# 1982 2006

#              Menu
# ==============================
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Enter your choice: 2

# Boston Americans:
# 1903

# New York Giants:
# 1905 1921 1922 1933 1954

# Chicago White Sox:
# 1906 1917 2005

# Chicago Cubs:
# 1907 1908

# Pittsburgh Pirates:
# 1909 1925 1960 1971 1979

# Philadelphia Athletics:
# 1910 1911 1913 1929 1930

# Boston Red Sox:
# 1912 1915 1916 1918 2004 2007

# Boston Braves:
# 1914

# Cincinnati Reds:
# 1919 1940 1975 1976 1990

# Cleveland Indians:
# 1920 1948

# New York Yankees:
# 1923 1927 1928 1932 1936 1937 1938 1939
# 1941 1943 1947 1949 1950 1951 1952 1953
# 1956 1958 1961 1962 1977 1978 1996 1998
# 1999 2000

# Washington Senators:
# 1924

# St. Louis Cardinals:
# 1926 1931 1934 1942 1944 1946 1964 1967
# 1982 2006

# Detroit Tigers:
# 1935 1945 1968 1984

# Brooklyn Dodgers:
# 1955

# Milwaukee Braves:
# 1957

# Los Angeles Dodgers:
# 1959 1963 1965 1981 1988

# Baltimore Orioles:
# 1966 1970 1983

# New York Mets:
# 1969 1986

# Oakland Athletics:
# 1972 1973 1974 1989

# Philadelphia Phillies:
# 1980 2008

# Kansas City Royals:
# 1985

# Minnesota Twins:
# 1987 1991

# Toronto Blue Jays:
# 1992 1993

# Atlanta Braves:
# 1995

# Florida Marlins:
# 1997 2003

# Arizona Diamondbacks:
# 2001

# Anaheim Angels:
# 2002

#              Menu
# ==============================
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Enter your choice: 3
# Enter a team's name: St. Louis Cardinals

# St. Louis Cardinals deleted

#              Menu
# ==============================
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Enter your choice: 4
# Enter a team's name: Florida Marlins
# Enter this team's new winning year(s): 1995 2008

# Florida Marlins updated

#              Menu
# ==============================
# 1. View a team's info
# 2. View all team's info
# 3. Delete a team's info
# 4. Change a team's info
# 5. Quit
# Enter your choice: 5
# Goodbye!

# ****************************************************************************************************

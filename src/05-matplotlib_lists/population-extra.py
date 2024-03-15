# ****************************************************************************************************
#
#       This program updates the population.py program to include a menu, more functions, and
#       plots both a bar chart and a line graph.
#
# ****************************************************************************************************

import matplotlib.pyplot as plt

# ****************************************************************************************************


def print_list(nums):
    for i in range(0, len(nums), 10):
        print(nums[i : i + 10])


# ****************************************************************************************************


def calc_difference(population_list):
    change_list = [
        population_list[i + 1] - population_list[i]
        for i in range(len(population_list) - 1)
    ]
    return change_list


# ****************************************************************************************************


def get_average(population_list):
    return sum(population_list) / len(population_list)


# ****************************************************************************************************


def get_greatest_increase(change_list):
    return max(change_list)


# ****************************************************************************************************


def get_smallest_increase(change_list):
    return min(change_list)


# ****************************************************************************************************


def plot_bar(population_list, start_year, end_year):
    left_edge = list(range(start_year, start_year + len(population_list)))
    plt.bar(left_edge, population_list)
    plt.xlabel("Year")
    plt.ylabel("Population (in thousands)")
    plt.title(f"US population chart ({start_year}-{end_year})")
    plt.show()


# ****************************************************************************************************


def plot_line(population_list, start_year, end_year):
    years = list(range(start_year, start_year + len(population_list)))
    plt.plot(years, population_list, "r--")
    plt.xlabel("Year")
    plt.ylabel("Population (in thousands)")
    plt.title(f"US population chart ({start_year}-{end_year})")
    plt.show()


# ****************************************************************************************************


def sort_ascending(change_list):
    asc_list = sorted(change_list)
    print_list(asc_list)


# ****************************************************************************************************


def sort_descending(change_list):
    desc_list = sorted(change_list, reverse=True)
    print_list(desc_list)


# ****************************************************************************************************


def search_pop(population_list):
    populate = int(input("Enter population(in thousands): "))

    if populate in population_list:
        print(f"\n{populate} found!")
    else:
        print(f"\n{populate} not found!")


# ****************************************************************************************************


def remove_pop(population_list, start_year, end_year):
    year_removed = int(input("Enter year: "))

    if start_year <= year_removed <= end_year:
        index = year_removed - start_year
        population_list[index] = 0

        if start_year <= year_removed < 1950:
            while population_list and population_list[0] == 0:
                population_list.pop(0)
                start_year += 1
        elif 1990 < year_removed <= end_year:
            while population_list and population_list[-1] == 0:
                population_list.pop()
                end_year -= 1

            print(f"\nPopulation for {year_removed} removed.")
    else:
        print("\nError: Year should be between either 1776-1950 and 1990-2023.")

    return start_year, end_year


# ****************************************************************************************************


def add_pop(population_list, start_year, end_year):
    year_add = int(input("Enter year: "))

    if 1776 <= year_add <= 2023:
        pop_add = int(input("Enter population(in thousands): "))

        if year_add < start_year:
            index = (start_year - year_add) - 1
            while index > 0:
                population_list.insert(0, 0)
                index -= 1
            population_list.insert(0, pop_add)
            start_year = year_add
        elif year_add > end_year:
            index = (year_add - end_year) - 1
            while index > 0:
                population_list.append(0)
                index -= 1
            population_list.append(pop_add)
            end_year = year_add
        else:
            index = (year_add - start_year) - 1
            population_list[index] = pop_add

        print(f"\n{pop_add} added for {year_add}.")
    else:
        print("\nError: Year should be between 1776 and 2023.")

    return start_year, end_year


# ****************************************************************************************************


def display_populations(population_list):
    print("\nPopulation List:")
    for year, pop in enumerate(population_list, 1950):
        print(f"{year}: {pop * 1000:,.0f}")


# ****************************************************************************************************


def menu(population_list):
    ch = 0
    start_year, end_year = 1950, 1990

    while ch != 12:
        try:
            print(f'\n{"Population Menu":^50}\n{"=" * 50}')
            print(
                " 1. Average Population\n"
                " 2. Greatest Population Increase\n"
                " 3. Smallest Population Increase\n"
                " 4. Bar Chart\n"
                " 5. Line Graph\n"
                " 6. Ascending Population Change\n"
                " 7. Descending Population Change\n"
                " 8. Search Population\n"
                " 9. Remove Population\n"
                "10. Add Population\n"
                "11. Display Populations\n"
                "12. Quit"
            )
            ch = int(input("Enter your choice: "))

            if ch == 1:
                avg_pop = get_average(population_list)
                print(f"\nAverage Population: {avg_pop * 1000:,.0f}")
            elif ch == 2:
                greatest_increase = get_greatest_increase(
                    calc_difference(population_list)
                )
                year_with_greatest_increase = start_year + calc_difference(
                    population_list
                ).index(greatest_increase)
                print(f"\nYear with Greatest Increase: {year_with_greatest_increase}")
            elif ch == 3:
                smallest_increase = get_smallest_increase(
                    calc_difference(population_list)
                )
                smallest_increase_year = start_year + calc_difference(
                    population_list
                ).index(smallest_increase)
                print(f"\nYear with Smallest Increase: {smallest_increase_year}")
            elif ch == 4:
                plot_bar(population_list, start_year, end_year)
            elif ch == 5:
                plot_line(population_list, start_year, end_year)
            elif ch == 6:
                print("\nSorted in Ascending Order:\n")
                sort_ascending(calc_difference(population_list))
            elif ch == 7:
                print("\nSorted in Descending Order:\n")
                sort_descending(calc_difference(population_list))
            elif ch == 8:
                search_pop(population_list)
            elif ch == 9:
                start_year, end_year = remove_pop(population_list, start_year, end_year)
            elif ch == 10:
                start_year, end_year = add_pop(population_list, start_year, end_year)
            elif ch == 11:
                display_populations(population_list)
            elif ch == 12:
                print("\nGoodbye!")
            else:
                raise ValueError(f"{ch} is not a valid choice.")

        except ValueError as ve:
            print(f"\nError: {ve}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")


# ****************************************************************************************************


def main():
    try:
        with open("USPopulation.txt", "r") as file:
            population_list = [int(line.strip()) for line in file]

        print_list(population_list)
        menu(population_list)

    except FileNotFoundError:
        print("The file could not be found.")
    except Exception:
        print("An error occurred.")


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************

# [151868, 153982, 156393, 158956, 161884, 165069, 168088, 171187, 174149, 177135]
# [179979, 182992, 185771, 188483, 191141, 193526, 195576, 197457, 199399, 201385]
# [203984, 206827, 209284, 211357, 213342, 215465, 217563, 219760, 222095, 224567]
# [227225, 229466, 231664, 233792, 235825, 237924, 240133, 242289, 244499, 246819]
# [249623]

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 11

# Population List:
# 1950: 151,868,000
# 1951: 153,982,000
# 1952: 156,393,000
# 1953: 158,956,000
# 1954: 161,884,000
# 1955: 165,069,000
# 1956: 168,088,000
# 1957: 171,187,000
# 1958: 174,149,000
# 1959: 177,135,000
# 1960: 179,979,000
# 1961: 182,992,000
# 1962: 185,771,000
# 1963: 188,483,000
# 1964: 191,141,000
# 1965: 193,526,000
# 1966: 195,576,000
# 1967: 197,457,000
# 1968: 199,399,000
# 1969: 201,385,000
# 1970: 203,984,000
# 1971: 206,827,000
# 1972: 209,284,000
# 1973: 211,357,000
# 1974: 213,342,000
# 1975: 215,465,000
# 1976: 217,563,000
# 1977: 219,760,000
# 1978: 222,095,000
# 1979: 224,567,000
# 1980: 227,225,000
# 1981: 229,466,000
# 1982: 231,664,000
# 1983: 233,792,000
# 1984: 235,825,000
# 1985: 237,924,000
# 1986: 240,133,000
# 1987: 242,289,000
# 1988: 244,499,000
# 1989: 246,819,000
# 1990: 249,623,000

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 10
# Enter year: 1995
# Enter population(in thousands): 250000

# 250000 added for 1995.

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 11

# Population List:
# 1950: 151,868,000
# 1951: 153,982,000
# 1952: 156,393,000
# 1953: 158,956,000
# 1954: 161,884,000
# 1955: 165,069,000
# 1956: 168,088,000
# 1957: 171,187,000
# 1958: 174,149,000
# 1959: 177,135,000
# 1960: 179,979,000
# 1961: 182,992,000
# 1962: 185,771,000
# 1963: 188,483,000
# 1964: 191,141,000
# 1965: 193,526,000
# 1966: 195,576,000
# 1967: 197,457,000
# 1968: 199,399,000
# 1969: 201,385,000
# 1970: 203,984,000
# 1971: 206,827,000
# 1972: 209,284,000
# 1973: 211,357,000
# 1974: 213,342,000
# 1975: 215,465,000
# 1976: 217,563,000
# 1977: 219,760,000
# 1978: 222,095,000
# 1979: 224,567,000
# 1980: 227,225,000
# 1981: 229,466,000
# 1982: 231,664,000
# 1983: 233,792,000
# 1984: 235,825,000
# 1985: 237,924,000
# 1986: 240,133,000
# 1987: 242,289,000
# 1988: 244,499,000
# 1989: 246,819,000
# 1990: 249,623,000
# 1991: 0
# 1992: 0
# 1993: 0
# 1994: 0
# 1995: 250,000,000

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 9
# Enter year: 1995

# Population for 1995 removed.

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 11

# Population List:
# 1950: 151,868,000
# 1951: 153,982,000
# 1952: 156,393,000
# 1953: 158,956,000
# 1954: 161,884,000
# 1955: 165,069,000
# 1956: 168,088,000
# 1957: 171,187,000
# 1958: 174,149,000
# 1959: 177,135,000
# 1960: 179,979,000
# 1961: 182,992,000
# 1962: 185,771,000
# 1963: 188,483,000
# 1964: 191,141,000
# 1965: 193,526,000
# 1966: 195,576,000
# 1967: 197,457,000
# 1968: 199,399,000
# 1969: 201,385,000
# 1970: 203,984,000
# 1971: 206,827,000
# 1972: 209,284,000
# 1973: 211,357,000
# 1974: 213,342,000
# 1975: 215,465,000
# 1976: 217,563,000
# 1977: 219,760,000
# 1978: 222,095,000
# 1979: 224,567,000
# 1980: 227,225,000
# 1981: 229,466,000
# 1982: 231,664,000
# 1983: 233,792,000
# 1984: 235,825,000
# 1985: 237,924,000
# 1986: 240,133,000
# 1987: 242,289,000
# 1988: 244,499,000
# 1989: 246,819,000
# 1990: 249,623,000

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 8
# Enter population(in thousands): 249623

# 249623 found!

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 7

# Sorted in Descending Order:

# [3185, 3099, 3019, 3013, 2986, 2962, 2928, 2844, 2843, 2804]
# [2779, 2712, 2658, 2658, 2599, 2563, 2472, 2457, 2411, 2385]
# [2335, 2320, 2241, 2210, 2209, 2198, 2197, 2156, 2128, 2123]
# [2114, 2099, 2098, 2073, 2050, 2033, 1986, 1985, 1942, 1881]

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 6

# Sorted in Ascending Order:

# [1881, 1942, 1985, 1986, 2033, 2050, 2073, 2098, 2099, 2114]
# [2123, 2128, 2156, 2197, 2198, 2209, 2210, 2241, 2320, 2335]
# [2385, 2411, 2457, 2472, 2563, 2599, 2658, 2658, 2712, 2779]
# [2804, 2843, 2844, 2928, 2962, 2986, 3013, 3019, 3099, 3185]

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 5

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 4

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 2

# Year with Greatest Increase: 1954

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 1

# Average Population: 202,876,171

#                  Population Menu
# ==================================================
#  1. Average Population
#  2. Greatest Population Increase
#  3. Smallest Population Increase
#  4. Bar Chart
#  5. Line Graph
#  6. Ascending Population Change
#  7. Descending Population Change
#  8. Search Population
#  9. Remove Population
# 10. Add Population
# 11. Display Populations
# 12. Quit
# Enter your choice: 12

# Goodbye!

# ****************************************************************************************************

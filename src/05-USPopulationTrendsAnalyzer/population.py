# ****************************************************************************************************
#
#       This program reads US population (in thousands) from a file and performs various operations
#       and plots a bar chart.
#
#       Other files required:
#         1.    USPopulation.txt - contains US population data from 1950 to 1990
#
# ****************************************************************************************************

import matplotlib.pyplot as plt


def print_list(nums):
    for i in range(0, len(nums), 10):
        print(nums[i : i + 10])


def calc_difference(population_list):
    return [
        population_list[i + 1] - population_list[i]
        for i in range(len(population_list) - 1)
    ]


def get_average(population_list):
    return sum(population_list) / len(population_list)


def get_greatest_increase(change_list):
    return max(change_list)


def get_smallest_increase(change_list):
    return min(change_list)


def plot_bar(population_list, start_year, end_year):
    left_edge = list(range(start_year, start_year + len(population_list)))
    plt.bar(left_edge, population_list)
    plt.xlabel("Year")
    plt.ylabel("Population (in thousands)")
    plt.title(f"US population chart ({start_year}-{end_year})")
    plt.show()


def sort_ascending(change_list):
    asc_list = sorted(change_list)
    print_list(asc_list)


def sort_descending(change_list):
    desc_list = sorted(change_list, reverse=True)
    print_list(desc_list)


def search_pop(population_list):
    populate = int(input("\nEnter population: "))

    if populate in population_list:
        print(f"\n{populate} found!")
    else:
        print(f"\n{populate} not found!")


def main():
    try:
        with open("USPopulation.txt", "r") as file:
            population_list = [int(line) for line in file]

        print_list(population_list)
        change_list = calc_difference(population_list)

        print("\nPopulation Changes:")
        print_list(change_list)

        avg_pop = get_average(population_list)
        print(f"\nAverage Population: {avg_pop * 1000:,.0f}")

        print(f"\nSmallest increase: {get_smallest_increase(change_list) * 1000:,.0f}")
        print(f"\nGreatest increase: {get_greatest_increase(change_list) * 1000:,.0f}")

        print("\nAscending order:")
        sort_ascending(change_list)

        print("\nDescending order:")
        sort_descending(change_list)

        search_pop(population_list)
        plot_bar(population_list, 1950, 1990)

    except FileNotFoundError:
        print("\nThe file could not be found.")
    except ValueError as ve:
        print(f"\nError: {ve}")
    except Exception:
        print("\nAn error occurred.")


if __name__ == "__main__":
    main()

# ****************************************************************************************************

# [151868, 153982, 156393, 158956, 161884, 165069, 168088, 171187, 174149, 177135]
# [179979, 182992, 185771, 188483, 191141, 193526, 195576, 197457, 199399, 201385]
# [203984, 206827, 209284, 211357, 213342, 215465, 217563, 219760, 222095, 224567]
# [227225, 229466, 231664, 233792, 235825, 237924, 240133, 242289, 244499, 246819]
# [249623]

# Population Changes:
# [2114, 2411, 2563, 2928, 3185, 3019, 3099, 2962, 2986, 2844]
# [3013, 2779, 2712, 2658, 2385, 2050, 1881, 1942, 1986, 2599]
# [2843, 2457, 2073, 1985, 2123, 2098, 2197, 2335, 2472, 2658]
# [2241, 2198, 2128, 2033, 2099, 2209, 2156, 2210, 2320, 2804]

# Average Population: 202,876,171

# Smallest increase: 1,881,000

# Greatest increase: 3,185,000

# Ascending order:
# [1881, 1942, 1985, 1986, 2033, 2050, 2073, 2098, 2099, 2114]
# [2123, 2128, 2156, 2197, 2198, 2209, 2210, 2241, 2320, 2335]
# [2385, 2411, 2457, 2472, 2563, 2599, 2658, 2658, 2712, 2779]
# [2804, 2843, 2844, 2928, 2962, 2986, 3013, 3019, 3099, 3185]

# Descending order:
# [3185, 3099, 3019, 3013, 2986, 2962, 2928, 2844, 2843, 2804]
# [2779, 2712, 2658, 2658, 2599, 2563, 2472, 2457, 2411, 2385]
# [2335, 2320, 2241, 2210, 2209, 2198, 2197, 2156, 2128, 2123]
# [2114, 2099, 2098, 2073, 2050, 2033, 1986, 1985, 1942, 1881]

# Enter population: 151868

# 151868 found!

# ****************************************************************************************************

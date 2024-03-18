# ****************************************************************************************************
#
#       This program will predict the approximate size of a population of organisms over a specific
#       period of time.
#
# ****************************************************************************************************


def populate(size, rate, days):
    # strings left-aligned by default
    print(f"\n{'Day':8}Population\n{'-' * 29}")

    for i in range(1, days + 1):
        print(f"{i:<8}{size}")
        size += size * rate


def main():
    size = int(input("Starting number of organisms: "))
    rate = float(input("Average daily increase: "))
    days = int(input("Number of days to multiply: "))

    populate(size, rate, days)


if __name__ == "__main__":
    main()

# ****************************************************************************************************

# Starting number of organisms: 100
# Average daily increase: 0.5
# Number of days to multiply: 10

# Day      Population
# -----------------------------
# 1        100
# 2        150.0
# 3        225.0
# 4        337.5
# 5        506.25
# 6        759.375
# 7        1139.0625
# 8        1708.59375
# 9        2562.890625
# 10       3844.3359375

# *****************************************************************************************************

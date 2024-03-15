from pet import Pet


def main():
    pet1 = Pet("dog", "Fido")
    pet2 = Pet("cat", "Fluffy")
    pet3 = Pet("bird", "Tweety")

    print(pet1, pet2, pet3, sep="\n")


if __name__ == "__main__":
    main()

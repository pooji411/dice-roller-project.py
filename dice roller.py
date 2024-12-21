import random
def roll_dice(num_dice, num_sides):
    """Rolls the specified number of dice with the specified number of sides"""
    return [random.randint(1, num_sides) for _ in range(num_dice)]


def main():
    print("Welcome to the Dice Roller!")

    while True:
        print("\n1. Roll a single six-sided die")
        print("2. Roll multiple six-sided dice")
        print("3. Roll a single die with a custom number of sides")
        print("4. Roll multiple dice with a custom number of sides")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = roll_dice(1, 6)
            print(f"You rolled a {result[0]}")
        elif choice == "2":
            num_dice = int(input("Enter the number of dice to roll: "))
            result = roll_dice(num_dice, 6)
            print(f"You rolled a {sum(result)} with rolls: {result}")
        elif choice == "3":
            num_sides = int(input("Enter the number of sides on the die: "))
            result = roll_dice(1, num_sides)
            print(f"You rolled a {result[0]}")
        elif choice == "4":
            num_dice = int(input("Enter the number of dice to roll: "))
            num_sides = int(input("Enter the number of sides on each die: "))
            result = roll_dice(num_dice, num_sides)
            print(f"You rolled a {sum(result)} with rolls: {result}")
        elif choice == "5":
            print("Exiting the Dice Roller. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


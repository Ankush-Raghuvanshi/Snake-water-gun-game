import random

# Computer randomly chooses from -1 (water), 0 (gun), 1 (snake)
Computer = random.choice([-1, 0, 1])

# Dictionary to map string input to game choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Input choice from user
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Ensure valid input
if youstr not in youDict:
    print("Invalid choice! Please choose 's' for snake, 'w' for water, or 'g' for gun.")
else:
    you = youDict[youstr]

    # Print choices
    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[Computer]}")

    # Determine the outcome
    if Computer == you:
        print("It's a draw")
    elif (Computer == 1 and you == -1) or (Computer == 0 and you == 1) or (Computer == -1 and you == 0):
        print("You lose")
    else:
        print("You win")

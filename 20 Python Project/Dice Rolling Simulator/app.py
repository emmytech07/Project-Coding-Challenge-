# Import Random
# Define a function to roll a dice
# Create a dictionary that eill have the drawing of the dice 
# Create a while asking user 
import random

def roll_dice():
    # Copied Dictionary
    DICE_ART = {
    1: (
        "┌─────────┐",
        "│    1    │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│    2    │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●   3  │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    4    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●  5 │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ● 6 ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
    roll = input("Roll a dice? (Yes/No) ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f'Dice rolled: {dice1}, {dice2}')
        print("\n".join(DICE_ART[dice1]))
        print("\n".join(DICE_ART[dice2]))
        # break
        roll = input("Roll a dice? (Yes/No) ")


roll_dice()
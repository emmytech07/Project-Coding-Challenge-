import random

exit = False

while exit == False:
    options = ['rocks', 'paper', 'scissors']
    userInput = input("Select rock, paper, scissor or exit: ")
    computerInput = random.choice(options)

    if userInput.lower() == "Exit".lower():
        print("Game Ended")
        print("Good bye")
        exit = True

    if userInput.lower() == 'rock'.lower():
        if computerInput.lower()=='rock'.lower():
            print("Your Input is Rock")
            print("Computer Input is Rock")
            print("It is a tie")
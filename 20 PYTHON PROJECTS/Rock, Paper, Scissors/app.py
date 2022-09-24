import random

exit = False
userPoint = 0
computerPoint = 0
while exit == False:
    options = ['rocks', 'paper', 'scissors']
    userInput = input("Select rock, paper, scissors or exit: ")
    computerInput = random.choice(options)

    if userInput == "Exit":
        print("Game Ended")
        print("Good bye")
        exit = True

    if userInput == 'rock':
        if computerInput =='rock':
            print("Your Input is Rock")
            print("Computer Input is Rock")
            print("It is a tie")

        elif computerInput=='paper':
            print("Your Input is rock")
            print("Computer Input is paper")
            print("Computer wins")
            computerPoint +=1

        elif computerInput=='scissors':
            print("Your Input is rock")
            print("Computer Input is Scissors")
            print("You win")
            userPoint +=1
    
    elif userInput == 'paper':
        if computerInput=='rock':
            print("Your Input is Paper")
            print("Computer Input is Rock")
            print("You win")
            userPoint +=1

        elif computerInput=='paper':
            print("Your Input is Paper")
            print("Computer Input is paper")
            print("It is a tie")
            

        elif computerInput=='scissors':
            print("Your Input is Paper")
            print("Computer Input is Scissors")
            print("Computer wins")
            computerPoint +=1
    
    elif userInput == 'scissors':
        if computerInput=='rock':
            print("Your Input is Scissors")
            print("Computer Input is Rock")
            print("Computer win")
            computerPoint +=1

        elif computerInput=='paper':
            print("Your Input is Scissors")
            print("Computer Input is paper")
            print("You win")
            userPoint +=1

        elif computerInput=='scissors':
            print("Your Input is Scissors")
            print("Computer Input is Scissors")
            print("It is a tie")
            
    elif userInput != 'rock' or userInput != 'scissors' or userInput != 'paper':
        print('Invalid input')
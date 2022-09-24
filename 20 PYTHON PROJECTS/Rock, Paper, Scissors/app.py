import random

exit = False
userPoint = 0
computerPoint = 0
while exit == False:
    options = ['rocks', 'paper', 'scissors']
    userInput = input("Select rock, paper, scissors or exit: ")
    computerInput = random.choice(options)

    if userInput.lower() == "Exit".lower():
        print("Game Ended")
        print("Good bye")
        exit = True

    if userInput.lower() == 'Rock'.lower():
        if computerInput.lower()=='rock'.lower():
            print("Your Input is Rock")
            print("Computer Input is Rock")
            print("It is a tie")

        elif computerInput.lower()=='paper'.lower():
            print("Your Input is rock")
            print("Computer Input is paper")
            print("Computer wins")
            computerPoint +=1

        elif computerInput.lower()=='Scissors'.lower():
            print("Your Input is rock")
            print("Computer Input is Scissors")
            print("You win")
            userPoint +=1
    
    elif userInput.lower() == 'Paper'.lower():
        if computerInput.lower()=='rock'.lower():
            print("Your Input is Paper")
            print("Computer Input is Rock")
            print("You win")
            userPoint +=1

        elif computerInput.lower()=='Paper'.lower():
            print("Your Input is Paper")
            print("Computer Input is paper")
            print("It is a tie")
            

        elif computerInput.lower()=='Scissors'.lower():
            print("Your Input is Paper")
            print("Computer Input is Scissors")
            print("Computer wins")
            computerPoint +=1
    
    elif userInput.lower() == 'Scissors'.lower():
        if computerInput.lower()=='rock'.lower():
            print("Your Input is Scissors")
            print("Computer Input is Rock")
            print("Computer win")
            computerPoint +=1

        elif computerInput.lower()=='Paper'.lower():
            print("Your Input is Scissors")
            print("Computer Input is paper")
            print("You win")
            userPoint +=1

        elif computerInput.lower()=='Scissors'.lower():
            print("Your Input is Scissors")
            print("Computer Input is Scissors")
            print("It is a tie")
            
    elif userInput.lower() != 'Rock'.lower() or userInput.lower() != 'Scissors'.lower() or userInput.lower() != 'Paper'.lower():
        print('Invalid input')
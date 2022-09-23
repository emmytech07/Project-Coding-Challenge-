


def addition(a, b):
    sum = a + b
    print(f"{a} + {b} = {sum}")
    print()

def subtraction(a, b):
    sub = a - b
    print(f"{a} - {b} = {sub}")
    print()

def Multiplication(a, b):
    mul = a * b
    print(f"{a} * {b} = {mul}")
    print()

def Division(a, b):
    div = a / b
    print(f"{a} - {b} / {div}")
    print()

while(True):
    print("SELECT OPTIONS FOR ANY OF THE OPERATIONS ")
    print("A: Addition")
    print("B: Subtraction")
    print("C: Multiplication")
    print("D: Division")
    print("E: Exit")
    print()

    choice = input("Input your choice: ")

    try:
        if choice == "A" or choice =='a':
            print('You Option for Addition')
            a = int(input("Input first number:  "))
            b = int(input("Input first number:  "))
            addition(a, b)

        elif choice == "B" or choice =='b':
            print('You Option for Subtraction')
            a = int(input("Input first number:  "))
            b = int(input("Input first number:  "))
            subtraction(a, b)

        elif choice == "C" or choice =='c':
            print('You Option for Multiplication')
            a = int(input("Input first number:  "))
            b = int(input("Input first number:  "))
            Multiplication(a, b)

        elif choice == "D" or choice =='d':
            print('You Option for Division')
            a = int(input("Input first number:  "))
            b = int(input("Input first number:  "))
            if b ==0:
                print("Value cannot be divisible by zero")
            else:
                Division(a, b)

        elif choice == "e" or choice== "E":
            print("logout by selecting option E")
            # quit()
        else:
            print("%s is not valid input. Please enter a, b ,c ,d or e." %choice)
    except ValueError:
        print("KINDLY SUPPLY VALUE, THANKS")
        quit()

    except TypeError:
        print("Expected value is not pass ")
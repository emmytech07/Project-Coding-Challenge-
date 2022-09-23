


def addition(a, b):
    sum = a + b
    print(f"{a} + {b} = {sum}")

def subtraction(a, b):
    sub = a + b
    print(f"{a} - {b} = {sub}")

def Multiplication(a, b):
    mul = a * b
    print(f"{a} * {b} = {mul}")

def Division(a, b):
    div = a / b
    print(f"{a} - {b} / {div}")

print("A: Addition")
print("B: Subtraction")
print("C: Multiplication")
print("D: Division")
print("E: Exit")

choice = input("Input your choice: ")

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
    division(a, b)

elif choice == "e" or choice== "E":
    print("program ended")
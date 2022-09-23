# Ask a user if they want to generate a password or not 
# If yes, ask for the password length,
# Generate the password 
# Print password 
# If iniitial response is not, exist  the program


import string
import random


# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.hexdigits)24
# print(string.__all__)

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()_+<>?:"{}')
print (characters)

def generate_password():
    password_length = int(input("Supply Your password length: "))

    random.shuffle(characters)
    
    password =[]

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate password? (Yes/No): ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Supply the correct options ")
def main():
    print("This is a Email Slicer Project ")
    print()
    mail = input("Supply your mail: ")
    (username, domain)= mail.split('@')
    (domain, extension) = domain.split('.')

    print(f"Username : {username}")
    print(f"domain : {domain}")
    print(f"Extension : {extension}")
    print()
    
while True:
    main()
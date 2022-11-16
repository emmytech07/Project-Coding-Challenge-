def main ():
    print("Conversion of Dollars to Pounds: ")
    print()
    print()

    dollars = eval(input("Enter amount in dollars: "))
    pounds = convertToPounds(dollars)
    print(pounds)

convertToPounds = lambda dollars: dollars * 0.82

main()
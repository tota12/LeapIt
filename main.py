import utils
#main menu
print("Welcome to the leap year checker!")
print("1. Check if a year is a leap year")
print("2. How many leap years are there between two years")
print("3. How leap years are calulated")
print("4. Exit")
choice = "0"
while choice != "4":
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Input a year and I'll tell you if it's a leap year or not.")
        year = utils.validate_year()
        #output
        if utils.is_leap(year):
            print(year, " is a leap year!")
        else:
            print(year, " isn't a leap year!")
    elif choice == "2":
        print("Input two years and I'll tell you how many leap years are there between them.")
        print("The start year: ")
        start_year = utils.validate_year()
        valid = False
        while not valid:
            print("The end year: ")
            end_year = utils.validate_year()
            if end_year > start_year:
                valid = True
            else:
                print("The end year must be greater than the start year.")
        print("There are ", utils.count_leap_years(start_year, end_year), " leap years between ", start_year, " and ", end_year, ".")
    elif choice == "3":
        print(utils.info)
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice")


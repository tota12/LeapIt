#checking if leap year
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

#counting leap years
def count_leap_years(start, end):
    count = 0
    for year in range(start, end):
        if is_leap(year):
            start = year
            break
    for i in range(start, end, 4):
        if is_leap(i):
            count += 1
    return count

# validate year
def validate_year():
    while True:
        try:
            year = int(input())
            if year <= 1582:
                print("Year must be greater than 1582 - the first year of Gregorian calendar.")
            else:
                break
        except ValueError:
            print("Please enter an integer")
    return year

# Leap year Info
info = """Leap years have 366 days instead of the regular 365 days.
The extra day is added in February, creating a new date: the 29th of February, which occurs once in four years.
The rule for calculating leap years is as follows:
  1- The year must be divisible by 4.
  2- If the year is divisible by 100, it must also be divisible by 400."""

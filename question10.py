#Write a program that take year as an input from user. Determine whether year is leap year
#or not.
def is_leap_year():
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year.")
    else:
        print(year, "is NOT a Leap Year.")

is_leap_year()

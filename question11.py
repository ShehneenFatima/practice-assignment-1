#Write a program that reads an integer and determines and prints whether it‟s odd or even.
def check_odd_even():
    num = int(input("Enter an integer: "))

    if num % 2 == 0:
        print(num, "is Even.")
    else:
        print(num, "is Odd.")

check_odd_even()

#Write a program that asks the user to enter two numbers, obtains them from the user and
#prints their sum, product, difference, quotient and remainder.
def calculate_operations():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Sum:", num1 + num2)
    print("Product:", num1 * num2)
    print("Difference:", num1 - num2)

    if num2 != 0:
        print("Quotient:", num1 / num2)
        print("Remainder:", num1 % num2)
    else:
        print("Division by zero is not possible.")

calculate_operations()

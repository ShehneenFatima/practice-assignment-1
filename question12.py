#12. Write a program that reads in two integers and determines and prints whether the first is a
#multiple of the second. [Hint: Use the remainder operator.
def check_multiple():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num2 == 0:
        print("Division by zero is not allowed.")
    elif num1 % num2 == 0:
        print(f"{num1} is a multiple of {num2}.")
    else:
        print(f"{num1} is NOT a multiple of {num2}.")

check_multiple()

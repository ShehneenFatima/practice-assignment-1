#The factorial of a non negative integer n is written n! (pronounced “n factorial”) and is
#defined as follows:
#n! = n · (n - 1) · (n - 2) · ... · 1 (for values of n greater than or equal to 1)
#and n! = 1 (for n = 0).
#For example, 5! = 5 · 4 · 3 · 2 · 1, which is 120.
#Write a program that take a number (n) from user, find and print factorial of that number.
def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

# Taking input from user
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")


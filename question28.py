# The factorial of a non-negative integer n is written as n! (pronounced “n factorial”) and is
# defined as follows:
# 
# n! = n × (n - 1) × (n - 2) × ... × 1 (for values of n ≥ 1)
# and n! = 1 (for n = 0).
#
# For example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120.
#
# Write a program that takes a number (n) from the user, calculates, and prints its factorial.

def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case: 0! = 1 and 1! = 1

    result = 1
    for i in range(2, n + 1):  # Loop from 2 to n
        result *= i

    return result

# Taking input from the user

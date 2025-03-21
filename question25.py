#Write a program to find the range of a set of numbers. Range is the difference between
#the smallest and biggest number in the list. You are not allowed to use built-in range()
#function.
def find_range():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]  # Convert input to a list of numbers

    smallest = min(numbers)
    largest = max(numbers)
    num_range = largest - smallest

    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
    print(f"Range: {num_range}")

find_range()

# Write a program that takes the side of a square from the user and prints the square using asterisks.
# The program should work for squares of all side sizes between 1 and 20.
#
# Example:
# If the user enters 4, the output should be:
# ****
# ****
# ****
# ****

def print_square(size):
    if size < 1 or size > 20:
        print("Please enter a size between 1 and 20.")
        return

    for _ in range(size):  # Loop for each row
        print("*" * size)  # Print a row of '*' with the given size

# Taking input from user
size = int(input("Enter the size of the square (1-20): "))

print_square(size)


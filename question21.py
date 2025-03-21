#21. Write a program that calculates the squares and cubes of the numbers from 0 to 10 and
#uses tabs to print the following table of values:
#number square cube
#0 0 0
#1 1 1
#2 4 8
#3 9 27
#4 16 64
#5 25 125
def print_square_cube_table():
    print("Number\tSquare\tCube")  # Header row
    for num in range(11):  # Loop from 0 to 10
        print(f"{num}\t{num**2}\t{num**3}")

print_square_cube_table()

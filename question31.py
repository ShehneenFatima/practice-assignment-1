# Write a program that displays the following checkerboard pattern:
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
#  * * * * * * * *

def print_checkerboard():
    for row in range(8):  # Loop for 8 rows
        if row % 2 == 0:
            print("* " * 8)  # Print stars for even rows
        else:
            print(" *" * 8)  # Print offset stars for odd rows

print_checkerboard()

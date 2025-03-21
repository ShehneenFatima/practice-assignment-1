#Write a program to find the binary equivalent of the entered number., i.e. binary
#equivalent of 170 is 10101010
def decimal_to_binary():
    num = int(input("Enter a decimal number: "))

    if num < 0:
        print("Please enter a non-negative integer.")
        return

    binary_equivalent = bin(num)[2:]  # Convert to binary and remove '0b' prefix
    print(f"Binary equivalent of {num} is {binary_equivalent}")

decimal_to_binary()

#If a five-digit number is input through the keyboard, write a program to calculate the sum
#of its digits. (Hint: Use the modulus operator „%‟ to split the digits).
def sum_of_digits():
    num = int(input("Enter a five-digit number: "))

    if num < 10000 or num > 99999:
        print("Invalid input! Please enter a five-digit number.")
        return

    digit1 = num % 10
    num //= 10
    digit2 = num % 10
    num //= 10
    digit3 = num % 10
    num //= 10
    digit4 = num % 10
    num //= 10
    digit5 = num % 10

    total = digit1 + digit2 + digit3 + digit4 + digit5

    print("Sum of digits:", total)

sum_of_digits()

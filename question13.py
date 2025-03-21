#Write a program that asks the user to enter two integers, obtains the numbers from the
#user, then prints the larger number followed by the words “is larger.” If the numbers are
#equal, print the message “These numbers are equal.” Use only the single-selection form
#of the if statement you learned in this chapter.
def compare_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    larger = num1  # Assume num1 is larger

    if num2 > num1:
        larger = num2

    if num1 != num2:
        print(f"{larger} is larger.")
    
    if num1 == num2:
        print("These numbers are equal.")

compare_numbers()

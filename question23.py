#23. Write a program to enter the numbers till the user wants and at the end it should display
#the count of positive, negative and zeros entered.
def count_numbers():
    pos_count = neg_count = zero_count = 0

    while True:
        try:
            num = input("Enter a number (or type 'stop' to finish): ")
            if num.lower() == 'stop':
                break

            num = float(num)

            if num > 0:
                pos_count += 1
            elif num < 0:
                neg_count += 1
            else:
                zero_count += 1

        except ValueError:
            print("Invalid input! Please enter a valid number or type 'stop' to finish.")

    print("\nResults:")
    print(f"Positive numbers: {pos_count}")
    print(f"Negative numbers: {neg_count}")
    print(f"Zeros: {zero_count}")

count_numbers()

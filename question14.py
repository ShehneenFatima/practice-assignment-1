#Write a program that inputs three different integers from the keyboard (i.e num1, num2,
#num3), then prints the sum, the average, the product, the smallest and the largest of these
#numbers.
def number_operations():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    total = num1 + num2 + num3
    average = total / 3
    product = num1 * num2 * num3
    smallest = min(num1, num2, num3)
    largest = max(num1, num2, num3)

    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Product: {product}")
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")

number_operations()

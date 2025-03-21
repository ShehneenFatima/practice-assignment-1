#Two numbers (base and exponent) are entered through the keyboard. Write a program to
#find the value of base raised to the power of exponent.
def power_calculation():
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent: "))

    result = base ** exponent

    print(f"{base} raised to the power {exponent} is: {result}")

power_calculation()


#Write a program to check whether a triangle is valid or not, when the three angles of the
#triangle are entered through the keyboard. A triangle is valid if the sum of all the three
#angles is equal to 180 degrees.
def is_valid_triangle():
    angle1 = float(input("Enter first angle: "))
    angle2 = float(input("Enter second angle: "))
    angle3 = float(input("Enter third angle: "))

    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        print("Invalid input! Angles must be positive numbers.")
        return

    total = angle1 + angle2 + angle3

    if total == 180:
        print("The triangle is valid.")
    else:
        print("The triangle is NOT valid.")

is_valid_triangle()

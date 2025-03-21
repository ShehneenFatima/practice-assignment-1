#19. If the three sides of a triangle are entered through the keyboard, write a program to check
#whether the triangle is isosceles, equilateral, scalene or right-angled triangle.
def check_triangle_type():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("The triangle is Equilateral.")
        elif a == b or b == c or a == c:
            print("The triangle is Isosceles.")
        elif round(a**2 + b**2, 2) == round(c**2, 2) or \
             round(b**2 + c**2, 2) == round(a**2, 2) or \
             round(a**2 + c**2, 2) == round(b**2, 2):
            print("The triangle is Right-Angled.")
        else:
            print("The triangle is Scalene.")
    else:
        print("Invalid triangle! The sum of any two sides must be greater than the third.")

check_triangle_type()

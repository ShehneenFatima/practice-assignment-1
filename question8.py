#Write a program that reads in the radius of a circle and prints the circle‟s diameter,
#circumference and area. Use the constant value 3.14159 for pi. Perform each of these
#calculations inside the print statement(s) and use the conversion format specifier %f.
def circle_properties():
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14159

    print("Diameter: %f" % (2 * radius))
    print("Circumference: %f" % (2 * pi * radius))
    print("Area: %f" % (pi * radius * radius))

circle_properties()

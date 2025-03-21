#The length & breadth of a rectangle are input through the keyboard. Write a program to
#calculate the area & perimeter of the rectangle.
def rectangle_calculations():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

rectangle_calculations()

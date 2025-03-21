#Given the length and breadth of a rectangle, write a program to find whether the area of
#the rectangle is greater than its perimeter. For example, the area of the rectangle with
#length = 5 and breadth = 4 is greater than its perimeter.
def compare_area_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    if length <= 0 or breadth <= 0:
        print("Invalid input! Length and breadth must be positive numbers.")
        return

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}")

    if area > perimeter:
        print("The area is greater than the perimeter.")
    else:
        print("The area is NOT greater than the perimeter.")

compare_area_perimeter()

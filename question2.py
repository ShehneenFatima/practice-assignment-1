#The distance between two cities (in km.) is input through the keyboard. Write a program
#to convert and print this distance in meters, feet, inches and centimeters.
def convert_distance():
    km = float(input("Enter distance in kilometers: "))

    meters = km * 1000
    feet = km * 3280.84
    inches = km * 39370.1
    centimeters = km * 100000

    print("Distance in meters:", meters)
    print("Distance in feet:", feet)
    print("Distance in inches:", inches)
    print("Distance in centimeters:", centimeters)

convert_distance()

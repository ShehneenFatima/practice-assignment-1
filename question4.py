#Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
#program to convert this temperature into Centigrade degrees.
def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", round(celsius, 2))

fahrenheit_to_celsius()

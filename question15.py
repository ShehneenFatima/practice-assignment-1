#(Body Mass Index Calculator) We introduced the body mass index (BMI) calculator in
#The formulas for calculating BMI are
#BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
#Create a BMI calculator application that reads the user‟s weight in kilograms and height
#in meters, then calculates and displays the user‟s body mass index. Also, the application

#should display the following information from the Department of Health and Human
#Services/National Institutes of Health so the user can evaluate his/her BMI:
#BMI VALUES
#Underweight: less than 18.5
#Normal: between 18.5 and 24.9
#Overweight: between 25 and 29.9
#Obese: 30 or greater
def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Invalid input! Weight and height must be positive numbers.")
        return

    bmi = weight / (height ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")

    print("\nBMI VALUES:")
    print("Underweight: less than 18.5")
    print("Normal: between 18.5 and 24.9")
    print("Overweight: between 25 and 29.9")
    print("Obese: 30 or greater")

    if bmi < 18.5:
        print("\nYou are Underweight.")
    elif 18.5 <= bmi < 24.9:
        print("\nYou have a Normal weight.")
    elif 25 <= bmi < 29.9:
        print("\nYou are Overweight.")
    else:
        print("\nYou are Obese.")

calculate_bmi()

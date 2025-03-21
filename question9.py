#9. A company insures its drivers in the following cases:
#− If the driver is married.
#− If the driver is unmarried, male & above 30 years of age.
#− If the driver is unmarried, female & above 25 years of age.
#In all other cases, the driver is not insured. If the marital status, sex and age of the driver
#are the inputs, write a program to determine whether the driver is to be insured or not.
def check_insurance():
    marital_status = input("Enter marital status (married/unmarried): ").strip().lower()
    gender = input("Enter gender (male/female): ").strip().lower()
    age = int(input("Enter age: "))

    if marital_status == "married":
        print("Driver is insured.")
    elif marital_status == "unmarried" and gender == "male" and age > 30:
        print("Driver is insured.")
    elif marital_status == "unmarried" and gender == "female" and age > 25:
        print("Driver is insured.")
    else:
        print("Driver is not insured.")

check_insurance()

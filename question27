# Develop a program that will determine the gross pay for each of several employees. 
# The company pays “straight time” for the first 40 hours worked by each employee 
# and pays “time-and-a-half” for all hours worked more than 40 hours. 
# You’re given a list of the employees of the company, the number of hours each employee 
# worked last week and the hourly rate of each employee. Your program should input this 
# information for each employee and should determine and display the employee's gross pay.
# 
# Sample input/output dialog:
# Enter # of hours worked (-1 to end): 39
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $390.00
# Enter # of hours worked (-1 to end): 40
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $400.00
# Enter # of hours worked (-1 to end): 41
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $415.00
# Enter # of hours worked (-1 to end): -1

def calculate_gross_pay():
    while True:
        hours_worked = float(input("Enter # of hours worked (-1 to end): "))
        if hours_worked == -1:
            break  # Exit loop if user enters -1

        hourly_rate = float(input("Enter hourly rate of the worker ($00.00): "))

        if hours_worked <= 40:
            salary = hours_worked * hourly_rate
        else:
            overtime_hours = hours_worked - 40
            salary = (40 * hourly_rate) + (overtime_hours * 1.5 * hourly_rate)

        print(f"Salary is ${salary:.2f}\n")

calculate_gross_pay()

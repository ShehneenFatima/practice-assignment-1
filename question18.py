#A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
#for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
#after 30days your membership will be cancelled. Write a program to accept the number
#of days the member is late to return the book and display the fine or the appropriate
#message.
def calculate_fine():
    days_late = int(input("Enter the number of days late: "))

    if days_late <= 0:
        print("No fine. Thank you for returning the book on time!")
    elif 1 <= days_late <= 5:
        fine = days_late * 0.50
        print(f"The fine is {fine:.2f} rupees.")
    elif 6 <= days_late <= 10:
        fine = days_late * 1
        print(f"The fine is {fine:.2f} rupees.")
    elif 11 <= days_late <= 30:
        fine = days_late * 5
        print(f"The fine is {fine:.2f} rupees.")
    else:
        print("Your membership has been cancelled due to late return of more than 30 days.")

calculate_fine()

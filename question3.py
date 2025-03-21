#Write a program that takes the marks obtained by a student in five different subjects as
#input through the keyboard, then find out the total marks and percentage marks obtained
#by the student in each subject. Assume that the maximum marks that can be obtained by a
#student in each subject is 100.
def calculate_marks():
    subjects = ["Math", "Science", "English", "History", "Computer"]
    marks = {}

    for subject in subjects:
        score = float(input(f"Enter marks for {subject} (out of 100): "))
        while score < 0 or score > 100:
            print("Invalid input! Marks should be between 0 and 100.")
            score = float(input(f"Enter marks for {subject} (out of 100): "))
        marks[subject] = score

    total_marks = sum(marks.values())
    percentage = (total_marks / 500) * 100

    print("\nTotal Marks:", total_marks)
    print("Percentage:", percentage, "%")

    for subject, score in marks.items():
        print(f"{subject}: {score} ({(score / 100) * 100}%)")

calculate_marks()

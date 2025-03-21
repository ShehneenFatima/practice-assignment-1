#A university has the following rules for a student to qualify for a degree with A as the
#main subject and B as the subsidiary subject:
#(a) He should get 55 percent or more in A and 45 percent or more in B.
#(b) If he gets than 55 percent in A he should get 55 percent or more in B. However, he
#should get at least 45 percent in A.
#(c) If he gets less than 45 percent in B and 65 percent or more in A he can reappear in an
#examination in B to qualify.
#(d) In all other cases he is declared to have failed.
def check_degree_qualification():
    A = float(input("Enter percentage marks in Subject A: "))
    B = float(input("Enter percentage marks in Subject B: "))

    if A >= 55 and B >= 45:
        print("Student qualifies for the degree.")
    elif A >= 45 and A < 55 and B >= 55:
        print("Student qualifies for the degree.")
    elif A >= 65 and B < 45:
        print("Student can reappear in Subject B to qualify.")
    else:
        print("Student has failed.")

check_degree_qualification()

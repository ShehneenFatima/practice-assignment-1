#Write a program to generate all combinations of 1, 2 and 3 using for loop.
def generate_combinations():
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                print(i, j, k)

generate_combinations()

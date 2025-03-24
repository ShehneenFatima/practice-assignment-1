#Diamond Problem
rows = 5  # Number of rows in the upper half

# Upper half of the diamond
for i in range(1, rows + 1, 2):
    print(" " * ((rows - i) // 2) + "*" * i)

# Lower half of the diamond
for i in range(rows - 2, 0, -2):
    print(" " * ((rows - i) // 2) + "*" * i)


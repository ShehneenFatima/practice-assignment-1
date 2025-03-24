# Triangle-Printing Program
# Prints four different triangle patterns side by side using loops.

# (A) Left-Aligned Right-Angled Triangle
print("(A)")
for i in range(1, 11):
    print("*" * i)
print()

# (B) Right-Aligned Right-Angled Triangle
print("(B)")
for i in range(10, 0, -1):
    print("*" * i)
print()

# (C) Centered Triangle (Pyramid)
print("(C)")
for i in range(10, 0, -1):
    print(" " * (10 - i) + "*" * i)
print()

# (D) Inverted Centered Triangle
print("(D)")
for i in range(1, 11):
    print(" " * (10 - i) + "*" * i)
print()

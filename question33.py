#In class, we discussed the logical operators and, or, and not. De Morgan‟s Laws can
#sometimes make it more convenient for us to express a logical expression. These lawss
#state that the expression not(condition1 and condition2) is logically equivalent to the
#expression (not(condition1)or not(condition2)). Also, the expression not(condition1
#orcondition2) is logically equivalent to the expression (not(condition1)and
#not(condition2)). Use De Morgan‟s Laws to write equivalent expressions for each of the
#following, and then write a program to show that both the original expression and the
#new expression in each case are equivalent.
#a) not( x <5 ) and not( y >= 7 )
#b) not( a == b ) or not( g != 5 )
#c) not( ( x <= 8 ) and ( y >4 ) )
#d) not( ( i >4 ) or ( j <= 6 ) )
def check_equivalence():
    x, y = 4, 7
    a, b = 3, 3
    g = 5
    i, j = 5, 6

    # (a) not( x <5 ) and not( y >= 7 )
    original_a = not (x < 5) and not (y >= 7)
    transformed_a = (x >= 5) or (y < 7)
    print(f"(a) {original_a} == {transformed_a}")

    # (b) not( a == b ) or not( g != 5 )
    original_b = not (a == b) or not (g != 5)
    transformed_b = (a != b) or (g == 5)
    print(f"(b) {original_b} == {transformed_b}")

    # (c) not( ( x <= 8 ) and ( y > 4 ) )
    original_c = not ((x <= 8) and (y > 4))
    transformed_c = (x > 8) or (y <= 4)
    print(f"(c) {original_c} == {transformed_c}")

    # (d) not( ( i > 4 ) or ( j <= 6 ) )
    original_d = not ((i > 4) or (j <= 6))
    transformed_d = (i <= 4) and (j > 6)
    print(f"(d) {original_d} == {transformed_d}")

check_equivalence()

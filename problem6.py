"""found the solution first try"""

def sum_of_squares(urm):
    return sum([x*x for x in range(urm+1)])  # an actual lovely solution for this

def squares_of_sum(urm):
    return sum(x for x in range(urm+1)) * sum(x for x in range(urm+1))

print("the difference is: " ,(squares_of_sum(100) - sum_of_squares(100)))
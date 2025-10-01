def pentagonal_numbers(count,starting=1):
    pentagonal_numbers = {}
    n=starting
    while True:
        number = n*(3*n-1)/2
        if n > count:
            break
        pentagonal_numbers[int(number)] = None
        n += 1

    return pentagonal_numbers
    # return n*(3*n-1)/2

i=1
smallest_difference = 99999999999
smallest_pk = 0
smallest_pj = 0
difference = 0

many_pentagon_numbers = pentagonal_numbers(10000)

for i in many_pentagon_numbers.keys():
    for j in many_pentagon_numbers.keys():
        value = i + j
        if value in many_pentagon_numbers:
            difference = abs(i - j)
            if difference in many_pentagon_numbers:
                smallest_difference = min(smallest_difference,difference)
print(smallest_difference)
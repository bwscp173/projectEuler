def square_digits(number):
    return sum([int(i)*int(i) for i in str(number)])

total=0
limit = 10000000
for i in range(limit):
    if i % 100000 == 0:
        print(f"{i}/{limit}: {total}")
    seen = {}
    starting_number = i
    while True:
        result = square_digits(starting_number)
        if result == 89:
            total += 1
            break
        if result in seen:
            break  #loop detected
        seen[result] = True
        starting_number = result

print(total)
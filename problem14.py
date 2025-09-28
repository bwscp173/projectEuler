def f(number):
    if number % 2 == 0:
        return number/2
    else:
        return (number*3)+1

def f2(starting_number):
    seen = 0
    while True:
        result = f(starting_number)
        seen += 1

        if result == 1:
            break
        
        starting_number = result
    
    return seen

total = {}
heighest_index = -1
heighest_value = -1
limit = 1000000

for i in range(1,limit):
    if i % 100000 == 0:
        print(f"{i}/{limit}: {total}")

    result = f2(i)
    if result>heighest_value:
        heighest_index = i
        heighest_value = result

print(heighest_index,heighest_value)
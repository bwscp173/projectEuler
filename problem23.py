def number_type(number):
    total = 0
    for i in range(1,int(number/2)+1):
        if number % i == 0:
            total += i
    if total > number:
        return "abundant"
    return None


abundant_numbers = [i for i in range(28123) if number_type(i) == "abundant"]
print("now adding")

all_abundant_added = {}
for i in abundant_numbers:
    for j in abundant_numbers:
        result = i + j
        if result >= 28123:
            break
        all_abundant_added[result]=None

print("now checking")

total = 0
for i in range(28123):
    if i not in all_abundant_added:
        total += i

print("answer:",total)
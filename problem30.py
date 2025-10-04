import math

def fifthPower(number):
    str_number = str(number)
    total = 0
    for i in range(len(str_number)):
        total += math.pow(int(str_number[i]),5)
        if total > number:
            return 0
    if total == number:
        print("found number:",number)
        return number
    return 0
total = 0
for i in range(2,1000_000):
    if i %10000 == 0:
        print(i,total)
    total += fifthPower(i)


print("total:",total)
    
#doing this one out of order as it looks ez
#did a better sultion for getting up to higher numbers
last_ten_digits = 0
temp=0
for i in range(1,1001):
    temp=i
    print(i)
    for j in range(1,i):
        temp *= i

    last_ten_digits += int(str(temp)[-10:])
    last_ten_digits = int(str(last_ten_digits)[-10:])

print(last_ten_digits)
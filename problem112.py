def increasing_number(number):
    sorted_number = [chr for chr in str(number)]
    sorted_number.sort()
    return ''.join(sorted_number) == str(number)

def decreasing_number(number):
    number = str(number)[::-1]
    sorted_number = [chr for chr in str(number)]
    sorted_number.sort()
    return ''.join(sorted_number) == str(number)

def bouncy_number(number):
    return not increasing_number(number) and not decreasing_number(number)

bouncy_count = 0
total = 0 
for i in range(1,999999999999):
    if bouncy_number(i):
        bouncy_count +=1
    total += 1
    if i % 100000 == 0:
        print(((bouncy_count/total)*100))

    if int((bouncy_count/total)*100) == 99:
        break

print(((bouncy_count/total)*100),i,bouncy_count,total)
print("the answer is:",total)
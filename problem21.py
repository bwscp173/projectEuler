
def amicable(number):
    total_amicable = 0
    for i in range(1,number):
        if number % i == 0:
            total_amicable +=i
    return total_amicable

total = 0
all_amicable_pairs = {}

for i in range(2,10000):
    result = amicable(i)
    all_amicable_pairs[i] = result
    if result in all_amicable_pairs and all_amicable_pairs[result] == i and i != result:
        
        total += i
        total += result
        
print(all_amicable_pairs)
print("total:",total)
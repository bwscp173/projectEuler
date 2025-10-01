import itertools
def number_type(number):
    total = 0
    for i in range(1,int(number**0.5)+1):
        if number % i == 0:
            total +=i
    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    else:
        return "deficient"
    

abundant_numbers = {}
non_abundant_numbers = []
for i in range(1,28124):
    if number_type(i) == "abundant":
        abundant_numbers[i] = None
    else:
        non_abundant_numbers.append(i)
total = 0
print(non_abundant_numbers[0])
# for i in non_abundant_numbers:
#     if i in abundant_numbers:
#         continue
#     for j in non_abundant_numbers:
#         if j in abundant_numbers:
#             continue
#         total += i + j
print(total)
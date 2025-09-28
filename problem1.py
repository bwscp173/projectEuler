"""Multiples of 3 or 5:
find the sum of all the mutiples of 3 or 5 below 1000"""

all_multiples:list[int] = []

for i in range(1000):
    if i*3 < 1000:
        all_multiples.append(i*3)
    if i*5 < 1000:
        all_multiples.append(i*5)


print(sum(all_multiples) - sum(range(0,1000,15)))
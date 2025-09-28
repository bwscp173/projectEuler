""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 
1 to 20
?"""

nums = [x for x in range(1,21)]

def checker(i):
    for x in nums:
        if i % x != 0:
            return False
    return True

i=0
while True:
    i += 1
    if checker(i):
        result = i
        break
print("result is: ", result)
# this one takes a sec to run
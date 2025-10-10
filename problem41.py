import math
import itertools

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True

def isPandigital(number):
    # no longer using this function as im using permutations
    for i in range(1,len(str(number))):
        if str(number).count(str(i)) != 1:
            return False
    return True

for i in range(8,1,-1):
    digits = ''.join([str(d) for d in range(1,i+1)])
    for perm in sorted(itertools.permutations(digits),reverse=True):
        number = int(''.join(perm))
        if isPrime(number):
            print("answer:",number)
            input()

print(isPandigital(7652413))
print(isPrime(7652413))
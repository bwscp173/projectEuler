"""The sum of the primes below 
10 is 2+3+5+7=17.

Find the sum of all the primes below two million."""

import math
def Eratosthenes(size=2_000_000):
    """my attempt at a Sieve of Eratosthenes without fully knowing what it is
    (i saw a short clip kinda explaing it)
    and you can be sure its my own code because it runs out of memory
    iv never had that happen before
    """
    allnumbers = []
    for i in range(size):
        allnumbers.append(i)


    for i in range(2,math.ceil(math.sqrt(size))):
        for j in range(2,size):
            if i*j >= size:
                break
            allnumbers[i*j] = 0

    return sum(allnumbers) - 1
print("the answer is: ",Eratosthenes())

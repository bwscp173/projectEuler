"""By listing the first six prime numbers: 
2,2,5,7,11 and 
13, we can see that the 
6th prime is 13.

What is the 
10001st prime number?"""

import math
def Eratosthenes(size=6000043):
    """my attempt at a Sieve of Eratosthenes without fully knowing what it is
    (i saw a short clip kinda explaing it)
    and you can be sure its my own code because it runs out of memory
    iv never had that happen before
    """
    allnumbers = []#[i for i in range(size)]
    #size=math.ceil(math.sqrt(size))
    for i in range(size):
        allnumbers.append(i)

    for i in range(2,math.ceil(math.sqrt(size))):
        for j in range(2,size):
            if i*j >= size:
                break
            allnumbers[i*j] = 0

    non_0 = []
    for i in range(len(allnumbers)):
        if allnumbers[i] != 0:
            non_0.append(allnumbers[i])
    return non_0[10001]
print("the answer is: ",Eratosthenes())

# took my trash 'solution' to problem 3 and just hard coded a randomly big-ish number + index
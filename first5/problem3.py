"""Largest Prime Factor:
what is the largest prime factor of the number 600851475143"""
import math
def Eratosthenes(size=600851475143):
    """my attempt at a Sieve of Eratosthenes without fully knowing what it is
    (i saw a short clip kinda explaing it)
    and you can be sure its my own code because it runs out of memory
    iv never had that happen before
    """
    allnumbers = []
    for i in range(size):
        if i % 10000000 == 0:
            print(f"still working ({i}/{size})")
        allnumbers.append(i)
    print("done with settingS")
    for i in range(2,math.ceil(math.sqrt(size))):

        for j in range(2,size):
            if i*j >= size:
                break

            allnumbers[i*j] = 0

    print(max(allnumbers))
Eratosthenes()
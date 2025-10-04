import math
def Eratosthenes(size=2_000_000):
    allnumbers = []
    for i in range(size):
        allnumbers.append(i)


    for i in range(2,math.ceil(math.sqrt(size))):
        for j in range(2,size):
            if i*j >= size:
                break
            allnumbers[i*j] = 0

    return allnumbers


primes = Eratosthenes()
for prime in primes:


    result = math.comb(prime,1)
    print(result)
    if result > 5000:
        print("answer:",prime)
        break
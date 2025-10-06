def isPrime(number):
    if number <= 1:
        return False
    for i in range(2,int(number/2)+1):
        if number%i == 0:
            return False
    return True


primes = [i for i in range(1001) if isPrime(i)]
highest_prime_index = 0
a_b = 0

for a in range(-999,1000):
    for b in primes:
        n = 0
        while isPrime((n**2)+(a*n)+b):
            n += 1
        if n > highest_prime_index:
            highest_prime_index = n-1
            a_b = a*b

print(a_b)


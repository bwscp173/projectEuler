def prime_sieve(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return primes

maximum = 50000000
total = set()

for i in prime_sieve(7072):
    if i**2 > maximum:
        print("breaking")
        break
    print(i) 
    for j in prime_sieve(368):
        if j**3 > maximum:
            break
        
        for k in prime_sieve(85):
            if k**4 > maximum:
                break
            value = i**2+j**3+k**4
            if value < maximum:
                total.add(value)
        
print("total:",len(total))
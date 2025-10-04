import math
def d(n):
    divisors=1  # setting to 1, as the range is only half of N
    for i in range(1,n//2+1):
        if n%i==0:
            divisors += 1
    return divisors

def M(n,k):
    max_divisor = 0
    for j in range(n,n+k):
        max_divisor = max(max_divisor,d(j))
    return max_divisor

def S(u,k):
    total = 0
    for n in range(1,u-k+2):
    # if n % 10 == 0:
        print(n,total)
        total += M(n,k)
    return total
print("the total is:",S(100_000_000,100_000))
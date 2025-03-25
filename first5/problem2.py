"""Even Fibonacci Numbers:
the sum of all even fibonacci numbers whose values do not exceed four million"""

#got this one first try!
evens = []
a=0
b=1

while a < 4000000:
    if b > a:
        a += b
        if a % 2 == 0:
            evens.append(a)
    elif b <= a:
        b += a
        if b % 2 == 0:
            evens.append(b)
    print(f"a:{a}, \tb:{b}")

print(sum(evens))
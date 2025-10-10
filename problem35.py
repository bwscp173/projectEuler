import math
def Eratosthenes(n):
    sieve = {i: True for i in range(2, n)}
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return {i: True for i, v in sieve.items() if v}

word=""
counter = 0
temp_counter = 0
siv = Eratosthenes(1_000_000)
for i in list(siv.keys()):
    word = str(i)
    print("i:",i)
    temp_counter = 0
    valid = True
    for j in range(1,len(word)):
        word = word[-1] + word[:-1]
        if int(word) not in siv:
            valid = False
            break
    if valid:
        print("found cool number:",i)
        counter += 1

print("answer:",counter)
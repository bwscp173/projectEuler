total = 0

for i in range(1,1_000_001):
    binary=bin(i)[2:]
    if str(i)==str(i)[::-1] and binary==binary[::-1]:
        total += i
print(total)
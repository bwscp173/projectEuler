
def is_stealthy(n: int) -> bool:
    sums = set()
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            b = n // a
            if (a + b - 1) in sums or (a + b + 1) in sums:
                return True
            sums.add(a + b)
    return False

total = 2851
uppervalue = int(10**14)
for n in range(int(10**6),uppervalue):
    if n % 10000 == 0:
        print(f"{n}/{uppervalue}({(n/uppervalue)*100}%)  -  {total}")
    if is_stealthy(n):
        total += 1

print("total: ",total)
fractional=[]
for i in range(1,1_000_000):
    fractional += str(i)
#print(fractional,type(fractional))
total = 1
for i in [1,10,100,1000,10000,100000]:
    print(fractional[i-1])
    total *= int(fractional[i-1])
print("answer:",total)
temp={}
for a in range(2,101):
    for b in range(2,101):
        temp[a**b] = None
print(len(temp))
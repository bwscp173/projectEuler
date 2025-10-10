import math

def hcf(num1,num2):
    return math.gcd(num1,num2)


answer = 0
for i in range(1_000_000):
    count = 0
    if i % 10000 == 0:
        print(f"{i}/{1_000_000} ({i/1_000_000*100}%)")
    for j in range(1,i+1):
        if hcf(i,j) == 1:
            count +=1
    try:
        answer = max(answer,i/count)
    except:
        pass
print("answer: ",answer)
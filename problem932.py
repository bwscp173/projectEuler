def T(n):
    sum=0
    temp=0
    for a in range(1,(int("9"*(n)))):
        #if a % 100==0:
        print(a,sum)
        for b in range(1,(int("9"*(n)))):
            temp=(a+b)*(a+b)
            if int(f"{a}{b}") == temp:
                sum += temp
    return sum

#print("answer:",T(4))
print("answer:",T(16))
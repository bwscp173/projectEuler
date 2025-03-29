"""A Pythagorean triplet is a set of three natural numbers, 
a<b<c, for which, aa+bb=cc
There exists exactly one Pythagorean triplet for which a+b+c=1000. find product abc"""


for a in range(1,1000):
    aa = a**2
    for b in range(1,1000):
        bb = b**2
        for c in range(1,1000):
            cc = c**2
            
            if (a + b + c == 1000) and (a<b<c) and (aa+bb==cc):
                print(a,b,c)
                print(aa,bb,cc)
                print(a*b*c)
                print("finished!")
                exit()
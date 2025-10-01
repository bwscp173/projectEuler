import itertools
perm = itertools.permutations((0,1,2,3,4,5,6,7,8,9))

total = 0
for number in perm:
    number = ''.join(map(str,number))
    if int(number[1:4]) % 2 == 0:    
        if int(number[2:5]) % 3 == 0:    
            if int(number[3:6]) % 5 == 0:    
                if int(number[4:7]) % 7 == 0:    
                    if int(number[5:8]) % 11 == 0:    
                        if int(number[6:9]) % 13 == 0:    
                            if int(number[7:10]) % 17 == 0:
                                total += int(number)

print("total:",total)
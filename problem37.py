def Eratosthenes(n):
    sieve = {i: True for i in range(2, n)}
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return {i: True for i, v in sieve.items() if v}

siv = Eratosthenes(1_000_000)
total = 0
temp_word = ""
for i in siv:
    if i in [2,3,5,7]:
        continue
    valid = True
    temp_word = str(i)
    temp_word_forward = str(i)
    temp_word_backwards = str(i)


    for j in range(len(str(i))-1):
        temp_word_forward=temp_word_forward[1:]
        temp_word_backwards=temp_word_backwards[:-1]
        #print(temp_word_backwards,temp_word_forward,i)
        if temp_word_forward == "" or temp_word_backwards=="":
            valid=False
            break

        if int(temp_word_backwards) in siv and int(temp_word_forward) in siv:
            pass
            #print("coool")
        else:
            valid=False

    if valid:
        print("found number:",i)
        total += i
print("answer:",total)
a = 1
b = 0
#toggle = False
index = 2

while True:
    if b>a:
        a = a + b
    else:
        b = a + b
    print(a,b)
    if index == 10:
        break
    #toggle = not toggle

    # if len(str(a)) >= 1000:
    #     print("a: ",a)
    #     break
    # if len(str(b)) >= 1000:
    #     print("b: ",b)
    #     break
    index += 1
print("index:",index)
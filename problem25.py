a = 1
b = 0
toggle = False
index = 2

while True:
    if toggle:
        a = a + b
    else:
        b = a + b
    toggle = not toggle

    if len(str(a)) >= 1000:
        print("a: ",a)
        break
    if len(str(b)) >= 1000:
        print("b: ",b)
        break
    index += 1
print("index:",index)
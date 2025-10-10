corners = [1]
end = (2*1001)-1
n = 2
i = 0
while end>len(corners):
    for _ in range(4):
        corners.append(corners[-1] + n)
        i+=1
    n+=2

print(sum(corners))
#removed this file as it is provided by project euler and takes up space
with open("0022_names.txt","r") as f:
    data = f.read().replace('"',"").split(",")

data.sort()

total = 0
index = 1
for name in data:
    name_value = sum([ord(chr)-64 for chr in name])

    total += name_value * index
    index += 1

print(total)
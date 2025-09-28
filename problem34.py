import math

digit_factorials = []
for i in range(3,1000000):
    factorial = [math.factorial(int(j)) for j in str(i)]
    if sum(factorial) == i:
        digit_factorials.append(i)

print(digit_factorials)
print(sum(digit_factorials))
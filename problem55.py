def check_palindrome(string):
    length = len(string)
    for i in range(0,length):
        if (string[i] != string[length-i-1]):
            return False
    return True

def lychrel_Number(number):
    index = 1
    while True:
        number = number + int(str(number)[::-1])
        is_palindrome = check_palindrome(str(number))
        if is_palindrome:
            return 0
        if index >= 50:
            return 1
        index += 1 


total = 0
for i in range(10000):
    total += lychrel_Number(i)

print("answer:",total)

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 
.

Find the largest palindrome made from the product of two 
3-digit numbers."""

def problem4():
    all_results = []
    for digit1 in range(999,99,-1):
        for digit2 in range(999,99,-1):
            result = str(digit1*digit2)
            if result[::-1] == result:
                all_results.append(int(result))
    return max(all_results)
if __name__ == "__main__":
    print("the answer is:",problem4())
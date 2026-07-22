import math

s = input().strip()
if sum(math.factorial(int(digit)) for digit in s) == int(s):
    print("Strong")
else:
    print("Not Strong")
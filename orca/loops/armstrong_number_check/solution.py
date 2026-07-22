s = input().strip()
d = len(s)
if sum(int(digit) ** d for digit in s) == int(s):
    print("Armstrong")
else:
    print("Not Armstrong")
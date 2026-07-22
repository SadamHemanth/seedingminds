n = input().strip()
if str(int(n) ** 2)[-1] == n[-1]:
    print("Automorphic")
else:
    print("Not Automorphic")
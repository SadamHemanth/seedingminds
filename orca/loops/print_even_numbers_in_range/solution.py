A, B = map(int, input().split())

found = False
for num in range(A, B + 1):
    if num % 2 == 0:
        print(num)
        found = True

if not found:
    print("None")
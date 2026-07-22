n = int(input())

if n == 1:
    print(0)
else:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    print(*fib[:n])
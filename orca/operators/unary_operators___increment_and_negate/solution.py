
try:
    N = int(input().strip())
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit(1)

if N < -1000 or N > 1000:
    print("Error: Number out of range (-1000 to 1000).")
    exit(1)

increment = N + 1
decrement = N - 1
negation = -N

print(increment)
print(decrement)
print(negation)
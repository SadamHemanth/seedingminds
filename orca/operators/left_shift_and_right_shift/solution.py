try:
    N, K = map(int, input().split())
except ValueError:
    print("Invalid input. Please enter two integers.")
    exit(1)

if not (0 <= N <= 1000 and 0 <= K <= 10):
    print("Input out of range.")
    exit(1)

left_shift = N << K  
right_shift = N >> K  
print(left_shift)
print(right_shift)
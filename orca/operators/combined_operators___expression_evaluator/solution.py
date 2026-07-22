def c_mod(a, b):
    return a - int(a / b) * b

try:
    A, B, C = map(int, input().split())
except ValueError:
    print("Invalid input. Please enter three integers.")
    exit(1)

if not (-100 <= A <= 100 and -100 <= B <= 100 and 1 <= C <= 100):
    print("Error: Inputs out of range.")
    exit(1)

result = (A + B) * C - c_mod(A, C)

print(result)
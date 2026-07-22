A, I = map(float, input().split())

tax = 0.0

if A < 60:
    if I <= 300000:
        tax = 0.0
    elif I <= 1000000:
        tax = (I - 300000) * 0.10
    else:
        tax = 70000 + (I - 1000000) * 0.20

elif A < 80:
    if I <= 500000:
        tax = 0.0
    elif I <= 1000000:
        tax = (I - 500000) * 0.10
    else:
        tax = 50000 + (I - 1000000) * 0.20

else:
    if I <= 1000000:
        tax = 0.0
    else:
        tax = (I - 1000000) * 0.20
print(f"{tax:.2f}")
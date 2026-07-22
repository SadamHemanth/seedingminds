U = int(input().strip())
if U <= 100:
    bill = U * 1.50
elif U <= 200:
    bill = 100 * 1.50 + (U - 100) * 2.50
elif U <= 300:
    bill = 100 * 1.50 + 100 * 2.50 + (U - 200) * 4.00
else:
    bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (U - 300) * 6.00
print(f"{bill:.2f}")
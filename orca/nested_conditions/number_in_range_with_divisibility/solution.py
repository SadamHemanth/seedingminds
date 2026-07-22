n = int(input())

if n < 1 or n > 100:
    print("Out of Range")
    exit(0)
else:
    if n % 2 == 0 and n % 3 == 0:
        print("Divisible by 6")
    elif n % 2 == 0:
        print("Divisible by 2")
    elif n % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not divisible by 2 or 3")

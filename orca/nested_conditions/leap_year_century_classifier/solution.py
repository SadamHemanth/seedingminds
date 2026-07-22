Y = int(input())
if Y % 100 == 0:
    if Y % 400 == 0:
        print("Century Leap Year")
    else:
        print("Century Normal Year")
else:
    if Y % 4 == 0:
        print("Non-Century Leap Year")
    else:
        print("Non-Century Normal Year")
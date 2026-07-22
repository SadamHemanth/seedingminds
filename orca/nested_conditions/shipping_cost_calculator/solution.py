w,z=map(float,input().split())
if z==1:
    if w<=5:
        print("50")
    elif w<=20:
        print("100")
    else:
        print("200")
elif z==2:
    if w<=5:
        print("100")
    elif w<=20:
        print("250")
    else:
        print("500")
elif z==3:
    if w<=5:
        print("500")
    elif w<=20:
        print("1500")
    else:
        print("3000")
else:
    print("Invalid Zone")
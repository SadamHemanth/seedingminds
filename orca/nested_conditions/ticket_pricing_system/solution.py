a,b=map(int,input().split())
if a<12:
    if 1<=b<=5:
       print("100")
    else:
       print("150")
elif 12<=a<=59:
    if 1<=b<=5:
       print("200")
    else:
       print("300")
else :
    if 1<=b<=5:
       print("150")
    else:
       print("200")
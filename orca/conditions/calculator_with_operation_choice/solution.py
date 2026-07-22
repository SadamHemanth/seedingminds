A,B=map(int,input().split())
c=input()
if c=='+' :
    print(A+B)
elif c=='-':
    print(A-B)
elif c=='*':
    print(A*B)
elif c=='/':
    if B==0:
        print("Error")
    else:
        print(f"{A/B:.2f}")
else:
    print("Error")
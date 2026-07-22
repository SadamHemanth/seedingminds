A,B,C=map(int,input().split())
if A+B > C and B+C > A and A+C > B:
    print("Valid")
else:
    print("Invalid")
N=int(input())
if N<0:
    if N%2==0:
       print("Negative Even")
    else:
      print("Negative Odd")
elif N>0:
    if N%2==0:
       print("Positive Even")
    else:
      print("Positive Odd")
else:
    print("Zero")

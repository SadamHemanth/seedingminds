N=int(input())
fact=N
x=1
if N!=0:
  for x in range (1,N):

     fact=x*fact
  print(fact)
else:
    print(1)
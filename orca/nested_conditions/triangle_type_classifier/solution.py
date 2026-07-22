A,B,C=map(int,input().split())
if A+B>C and A+C>B and B+C>A:
   if A==B==C:
    print("Equilateral")
   elif A==B or B==A or C==A:
    print("Isosceles")
   elif A!=B!=C:
    print("Scalene")
   else:
    print("Invalid")
else:
    print("Invalid")
X, Y = map(int, input().split())
if X == 0 and Y == 0:
    print("Origin")
elif Y == 0:
    print("X-Axis")
elif X == 0:
    print("Y-Axis")
elif X > 0 and Y > 0:
    print("Q1")
elif X < 0 and Y > 0:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
else:
    print("Q4")
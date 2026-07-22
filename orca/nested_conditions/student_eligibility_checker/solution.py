M, P, C = map(int, input().split())
if M >= 65 and P >= 55 and C >= 50:
    total_three = M + P + C
    total_math_physics = M + P
    if total_three >= 190 or total_math_physics >= 140:
        print("Eligible")
    else:
        print("Failed Total Criteria")
else:
    print("Failed Subject Criteria")
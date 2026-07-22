A = int(input().strip())
if A < 0 or A > 150:
    print("Invalid")
elif 0 <= A <= 2:
    print("Infant")
elif 3 <= A <= 12:
    if 3 <= A <= 7:
        print("Child (Junior)")
    else:
        print("Child (Senior)")
elif 13 <= A <= 17:
    print("Teenager")
elif 18 <= A <= 59:
    if 18 <= A <= 35:
        print("Adult (Young)")
    else:  
        print("Adult (Middle)")
else: 
    print("Senior Citizen")
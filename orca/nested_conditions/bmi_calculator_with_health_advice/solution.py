w, h = map(float, input().split())
bmi = w / (h * h)

if bmi < 18.5:
    print(f"{bmi:.1f}")
    print("Underweight")
elif 18.5 <= bmi < 25.0:
    print(f"{bmi:.1f}")
    print("Normal")
elif 25.0 <= bmi < 30.0:
    print(f"{bmi:.1f}")
    print("Overweight")
else:
    print(f"{bmi:.1f}")
    print("Obese")

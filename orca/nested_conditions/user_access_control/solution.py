
input_data = input().split()
S, F = input_data[0], input_data[1]

valid_tiers = ["free", "pro", "enterprise"]
valid_features = ["basic", "advanced", "premium"]

if S not in valid_tiers:
    print("Invalid Tier")
elif F not in valid_features:
    print("Invalid Feature")
else:
    if S == "free":
        if F == "basic":
            print("Access Granted")
        else:
            print("Upgrade Required")
    elif S == "pro":
        if F in ["basic", "advanced"]:
            print("Access Granted")
        else:
            print("Upgrade Required")
    elif S == "enterprise":
        print("Access Granted")
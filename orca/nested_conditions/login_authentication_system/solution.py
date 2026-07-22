Username = input()

if Username == "admin":
    Password = input()
    if Password == "secret123":
        print("Login Successful")
    else:
        print("Incorrect Password")
elif Username == "guest":
    print("Guest Access Granted")
else:
    print("User Not Found")

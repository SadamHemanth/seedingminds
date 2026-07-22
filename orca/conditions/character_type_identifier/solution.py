C = input().strip()
if 'A' <= C <= 'Z':
    print("Uppercase Alphabet")
elif 'a' <= C <= 'z':
    print("Lowercase Alphabet")
elif '0' <= C <= '9':
    print("Digit")
else:
    print("Special Character")
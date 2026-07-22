s, l = map(int, input().split())

if s < l:
    print("No Fine")
elif s == l:
    print("No Fine")
elif l + 1 < s <= l + 10:
    print("Fine: 500")
elif l + 11 <= s <= l + 20:
    print('Fine: 1000')
else:
    print("Fine: 2000")
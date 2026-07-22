
n = int(input())
total_characters = 0
for i in range(n):
    line = input()
    total_characters = total_characters + len(line)

print(total_characters)

M, Y = map(int, input().split())
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if M == 2 and is_leap_year(Y):
    print(29)
else:
    print(days_in_month[M-1])
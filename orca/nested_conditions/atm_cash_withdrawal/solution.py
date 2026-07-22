data = input().split()
B = int(data[0])
T = data[1].strip().lower()
W = int(data[2])
if T == 'savings':
    limit = 20000
else:
    limit = 50000
if W > limit:
    print("Transaction Limit Exceeded")
elif W > B:
    print("Insufficient Balance")
else:
    new_balance = B - W
    print(f"Withdrawal Successful: {new_balance}")
cp, sp = map(float, input().split())

if sp > cp:
    profit_percent = ((sp - cp) / cp) * 100
    print(f"Profit of {profit_percent:.2f}%")
elif sp < cp:
    loss_percent = ((cp - sp) / cp) * 100
    print(f"Loss of {loss_percent:.2f}%")
else:
    print("No Profit No Loss")

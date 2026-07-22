player1 = input()
player2 = input()

if player1 == player2:
    print("Draw")
else:
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")

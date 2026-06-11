import random

choices = ["r", "p", "s"]

# What defeats what
counter = {
    "r": "p",
    "p": "s",
    "s": "r"
}

# Computer starts randomly
computer = random.choice(choices)

wins = 0
losses = 0
draws = 0

print("r = Rock")
print("p = Paper")
print("s = Scissors")

while True:

    user = input("\nChoose (r/p/s) or q to quit: ").lower()

    if user == "q":
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    print(f"User: {user}  vs  Computer: {computer}")

    # ---------- RESULT ----------
    if user == computer:
        print("0 -> Tie")
        draws += 1
        result = "tie"

    elif (
        (user == "r" and computer == "s") or
        (user == "p" and computer == "r") or
        (user == "s" and computer == "p")
    ):
        print("1 -> User Wins")
        wins += 1
        result = "user"

    else:
        print("-1 -> Computer Wins")
        losses += 1
        result = "computer"

    # ---------- SCORE ----------
    print(f"Wins: {wins} | Losses: {losses} | Draws: {draws}")

    # ---------- COMPUTER STRATEGY ----------
    if result == "computer":
        # If computer won → copy user's move
        computer = user

    else:
        # If computer lost or tied → counter user's move
        computer = counter[user]
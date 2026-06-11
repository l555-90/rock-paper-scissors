import random

choices = ["r", "p", "s"]

# What defeats what
counter = {
    "r": "p",   # paper beats rock
    "p": "s",   # scissors beats paper
    "s": "r"    # rock beats scissors
}

# Computer starts randomly
computer = random.choice(choices)

# Keep track of previous round
previous_user = None
previous_result = None

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
        print("0  -> Tie")
        result = "tie"

    elif (
        (user == "r" and computer == "s") or
        (user == "p" and computer == "r") or
        (user == "s" and computer == "p")
    ):
        print("1  -> User Wins")
        result = "user"

    else:
        print("-1 -> Computer Wins")
        result = "computer"

    # ---------- COMPUTER STRATEGY ----------
    # Use previous round to decide next move

    if result == "computer":
        # If computer won:
        # choose what user chose before
        next_computer = user

    elif result == "user":
        # If computer lost:
        # counter user's previous throw
        next_computer = counter[user]

    else:
        # If tie:
        # counter user's previous throw
        next_computer = counter[user]

    # Update computer move for next round
    computer = next_computer
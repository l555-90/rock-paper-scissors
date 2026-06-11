import tkinter as tk
import random

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x450")

# ---------------- GAME DATA ----------------
choices = ["Rock", "Paper", "Scissors"]

time_left = 3
game_active = False

wins = 0
losses = 0
draws = 0

# ---------------- LABELS ----------------
title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20)
)
title_label.pack(pady=10)

timer_label = tk.Label(
    root,
    text="Time Left: 3",
    font=("Arial", 14)
)
timer_label.pack()

score_label = tk.Label(
    root,
    text="Wins: 0   Losses: 0   Draws: 0",
    font=("Arial", 13)
)
score_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="Press START to play",
    font=("Arial", 12),
    justify="center"
)
result_label.pack(pady=20)

# ---------------- FUNCTIONS ----------------

def update_score():
    score_label.config(
        text=f"Wins: {wins}   Losses: {losses}   Draws: {draws}"
    )

def countdown():
    global time_left, game_active, losses

    if game_active:
        if time_left > 0:
            timer_label.config(text=f"Time Left: {time_left}")
            time_left -= 1
            root.after(1000, countdown)

        else:
            timer_label.config(text="TIME OUT!")
            result_label.config(text="You ran out of time!")

            losses += 1
            update_score()

            game_active = False

def start_game():
    global time_left, game_active

    # Prevent restarting while already playing
    if game_active:
        return

    time_left = 3
    game_active = True

    timer_label.config(text="Time Left: 3")
    result_label.config(text="Choose Rock, Paper, or Scissors")

    countdown()

def choose(player_choice):
    global wins, losses, draws, game_active

    if not game_active:
        return

    game_active = False

    computer_choice = random.choice(choices)

    # RESULT CHECK
    if player_choice == computer_choice:
        result = "It's a Draw!"
        draws += 1

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        wins += 1

    else:
        result = "Computer Wins!"
        losses += 1

    update_score()

    result_label.config(
        text=f"You chose: {player_choice}\n"
             f"Computer chose: {computer_choice}\n\n"
             f"{result}"
    )

# ---------------- BUTTONS ----------------

rock_button = tk.Button(
    root,
    text="Rock",
    width=15,
    height=2,
    command=lambda: choose("Rock")
)
rock_button.pack(pady=5)

paper_button = tk.Button(
    root,
    text="Paper",
    width=15,
    height=2,
    command=lambda: choose("Paper")
)
paper_button.pack(pady=5)

scissors_button = tk.Button(
    root,
    text="Scissors",
    width=15,
    height=2,
    command=lambda: choose("Scissors")
)
scissors_button.pack(pady=5)


root.bind("<Button-1>", lambda event: start_game())
# ---------------- RUN ----------------
root.mainloop()
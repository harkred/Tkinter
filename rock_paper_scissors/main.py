import tkinter as tk
from tkinter import ttk
import random

def engine(choice):
    global player_score, comp_score
    #win_mat[player choice][comp choice]
    #0-Loss 1-Won -1-Draw
    win_mat = [
        [-1, 0, 1],
        [1, -1, 0],
        [0, 1, -1]
    ]

    comp_choice = random.randint(-1, 1)
    if win_mat[choice][comp_choice] == 1:
        winner = "Player"
        player_score += 1

    elif win_mat[choice][comp_choice] == 0:
        winner = "Computer"
        comp_score += 1

    elif win_mat[choice][comp_choice] == -1:
        winner = "No One"

    outcome.config(text=f"Winner is the {winner}")
    pscore.config(text=f"Player Score: {str(player_score)}")
    cscore.config(text=f"Computer Score: {str(comp_score)}")

#Window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.resizable(0, 0)

#Main Frame
main_frame = ttk.LabelFrame(root, text="Play")
main_frame.pack(fill=tk.BOTH, expand=1)

#Buttons
ttk.Button(main_frame, text="Rock", command=lambda:engine(0)).grid(row=0, column=0)
ttk.Button(main_frame, text="Paper", command=lambda:engine(1)).grid(row=0, column=1)
ttk.Button(main_frame, text="Scissor", command=lambda:engine(2)).grid(row=0, column=2)

#Winner frame
win_frame = ttk.LabelFrame(main_frame, text="Outcome")
win_frame.grid(row=1, column=0, columnspan=3)

outcome = ttk.Label(win_frame, text="Winner is player")
outcome.pack(fill=tk.X, expand=1)

#Score frame
score_frame = ttk.LabelFrame(main_frame, text="Scores")
score_frame.grid(row=2, column=0, columnspan=3)


player_score = 0
comp_score = 0

pscore = ttk.Label(score_frame, text=f"Player Score: {str(player_score)}")
cscore = ttk.Label(score_frame, text=f"Computer Score: {str(comp_score)}")
pscore.pack(side=tk.LEFT, padx=10)
cscore.pack(side=tk.RIGHT, padx=10)

tk.mainloop()
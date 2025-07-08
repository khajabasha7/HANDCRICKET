import tkinter as tk
from tkinter import messagebox
import random

user_score = 0
comp_score = 0
user_batting = True
game_started = False

def show_rules():
    rules = (
        "📝 Game Rules:\n"
        "- Toss first to decide who plays.\n"
        "- Batting: Score runs by choosing numbers 1–6.\n"
        "- If your number matches the computer's, you're OUT!\n"
        "- Then, bowling starts (and vice versa).\n"
        "- The one with the highest score wins!"
    )
    messagebox.showinfo("Game Rules", rules)

def toss():
    global user_batting, game_started
    game_started = True
    toss_result = random.choice(["Head", "Tail"])
    user_call = toss_var.get()

    if user_call == toss_result:
        choice = messagebox.askquestion("Toss Result", "You won the toss! Do you want to Bat?")
        user_batting = (choice == 'yes')
    else:
        user_batting = random.choice([True, False])
        messagebox.showinfo("Toss Result", f"Computer won the toss and chose to {'Bat' if user_batting == False else 'Bowl'}")

    update_scoreboard()
    game_area.config(text="Game Started! Select a number (1-6) to play your move.")

def play(user_input):
    global user_score, comp_score, user_batting, game_started
    if not game_started:
        messagebox.showinfo("Info", "Start the game by tossing first.")
        return

    comp_input = random.randint(1, 6)
    if user_batting:
        if user_input == comp_input:
            game_area.config(text=f"OUT! You: {user_input} | Comp: {comp_input}")
            user_batting = False
        else:
            user_score += user_input
            game_area.config(text=f"You: {user_input} | Comp: {comp_input} ➤ You Scored!")
    else:
        if user_input == comp_input:
            game_area.config(text=f"Computer OUT! You: {user_input} | Comp: {comp_input}")
            check_winner()
            return
        else:
            comp_score += comp_input
            game_area.config(text=f"You: {user_input} | Comp: {comp_input} ➤ Computer Scored!")

    update_scoreboard()

def check_winner():
    global game_started
    game_started = False
    if user_score > comp_score:
        messagebox.showinfo("Result", f"You Win! 🏆\nYour Score: {user_score} | Comp: {comp_score}")
    elif user_score < comp_score:
        messagebox.showinfo("Result", f"Computer Wins! 🤖\nYour Score: {user_score} | Comp: {comp_score}")
    else:
        messagebox.showinfo("Result", f"It's a Tie! 🤝\nYour Score: {user_score} | Comp: {comp_score}")
    update_scoreboard()

def update_scoreboard():
    scoreboard.config(text=f"🏏 You: {user_score}   🤖 Comp: {comp_score}")

def play_again():
    global user_score, comp_score, user_batting, game_started
    user_score = 0
    comp_score = 0
    user_batting = True
    game_started = False
    update_scoreboard()
    game_area.config(text="Toss to start a new game!")

def quit_game():
    root.destroy()

root = tk.Tk()
root.title("Hand Cricket Game")
root.geometry("400x600")
root.configure(bg="#1f1f2e")

tk.Label(root, text="Hand Cricket 🏏", font=("Helvetica", 22, "bold"), bg="#1f1f2e", fg="white").pack(pady=15)

tk.Button(root, text="📖 Rules", command=show_rules, font=("Helvetica", 12, "bold"),
          bg="#f39c12", fg="white", width=15).pack(pady=5)

tk.Label(root, text="🪙 Choose Head or Tail:", font=("Helvetica", 13, "bold"),
         bg="#1f1f2e", fg="white").pack(pady=(15, 5))

toss_frame = tk.Frame(root, bg="#2c2c3a", bd=2, relief="ridge", padx=10, pady=5)
toss_var = tk.StringVar(value="Head")

tk.Radiobutton(toss_frame, text="Head", variable=toss_var, value="Head",
               font=("Helvetica", 12), bg="#2c2c3a", fg="white", selectcolor="#444").pack(side="left", padx=15)
tk.Radiobutton(toss_frame, text="Tail", variable=toss_var, value="Tail",
               font=("Helvetica", 12), bg="#2c2c3a", fg="white", selectcolor="#444").pack(side="left", padx=15)

toss_frame.pack(pady=5)


tk.Button(root, text="🪙 Toss", command=toss, bg="#2980b9", fg="white",
          font=("Helvetica", 12, "bold"), width=15).pack(pady=5)

game_area = tk.Label(root, text="Toss to start the game.", font=("Helvetica", 12), wraplength=350,
                     fg="white", bg="#1f1f2e", height=3)
game_area.pack(pady=10)

btn_frame = tk.Frame(root, bg="#1f1f2e")
for i in range(1, 7):
    btn = tk.Button(btn_frame, text=str(i), width=5, height=2,
                    font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white",
                    command=lambda x=i: play(x))
    btn.grid(row=(i-1)//3, column=(i-1)%3, padx=10, pady=10)
btn_frame.pack(pady=10)


scoreboard = tk.Label(root, text="🏏 You: 0   🤖 Comp: 0", font=("Helvetica", 13, "bold"),
                      fg="white", bg="#1f1f2e")
scoreboard.pack(pady=15)

control_frame = tk.Frame(root, bg="#1f1f2e")
tk.Button(control_frame, text="🔁 Play Again", command=play_again, bg="#8e44ad",
          fg="white", font=("Helvetica", 12, "bold"), width=12).pack(side="left", padx=10)
tk.Button(control_frame, text="🚪 Quit", command=quit_game, bg="#c0392b",
          fg="white", font=("Helvetica", 12, "bold"), width=8).pack(side="left", padx=10)
control_frame.pack(pady=15)

root.mainloop()

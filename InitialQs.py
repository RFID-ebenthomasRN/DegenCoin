import tkinter as tk
from tkinter import simpledialog

# Function to ask game settings
def get_game_settings():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    name = simpledialog.askstring("Input", "What is the name of the game?")
    num_vars = simpledialog.askinteger("Input", "How many variables are there?")
    variables = []
    for i in range(num_vars):
        var_name = simpledialog.askstring("Input", f"What is variable {i+1} name?")
        var_val = simpledialog.askinteger("Input", f"What is variable {i+1} value?")
        var_win_perc = simpledialog.askfloat("Input", f"What is variable {i+1} chance of winning (in percentage)?")
        var_rng = simpledialog.askstring("Input", f"What is variable {i+1} RNG range (e.g., '1-100')?")
        variables.append([var_name, var_val, var_win_perc, tuple(map(int, var_rng.split('-')))])
    return name, variables

game_name, game_variables = get_game_settings()
import os

directory = '/Users/apple/PycharmProjects/USERcRaTED'
if not os.path.exists(directory):
    os.makedirs(directory)

files = {
    'game_config.py': """
import tkinter as tk
from tkinter import simpledialog

def get_game_settings():
    root = tk.Tk()
    root.withdraw()
    name = simpledialog.askstring("Input", "What is the name of the game?")
    num_vars = simpledialog.askinteger("Input", "How many variables are there?")
    variables = []
    for i in range(num_vars):
        var_name = simpledialog.askstring("Input", f"What is variable {i+1} name?")
        var_val = simpledialog.askinteger("Input", f"What is variable {i+1} value?")
        var_win_perc = simpledialog.askfloat("Input", f"What is variable {i+1} chance of winning (in percentage)?")
        var_rng = simpledialog.askstring("Input", f"What is variable {i+1} RNG range (e.g., '1-100')?")
        variables.append([var_name, var_val, var_win_perc, tuple(map(int, var_rng.split('-')))])
    return name, variables """,

    'game_database.py': """
import sqlite3

class GameDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('game.db')
        self.cursor = self.conn.cursor()

    def _execute_query(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        self.conn.commit()

    def close_connection(self):
        self.conn.close() """,

    'model_builder.py': """
from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.optimizers import Adam

class ModelBuilder:
    @staticmethod
    def build_model():
        model = Sequential()
        model.add(LSTM(50, input_shape=(None, 1)))
        model.add(Dense(1, activation='sigmoid'))
        opt = Adam(learning_rate=0.01)
        model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
        return model """,

    'variable_predictor.py': """
class VariablePredictor:

    def __init__(self):
        # To be implemented...
        pass

    def predict_next(self):
        # To be implemented...
        pass """,

    'main_app.py': """
import tkinter as tk

class MainApp:
    def __init__(self, root):
        # To be implemented...
        pass

def run_app():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    run_app() """,

    'visualizer.py': """
class Visualizer:
    def __init__(self):
        # To be implemented...
        pass

    def draw_chart(self):
        # To be implemented...
        pass """,

    'game_utils.py': """
def get_random_number():
    # To be implemented...
    pass

def save_game():
    # To be implemented...
    pass

def load_game():
    # To be implemented...
    pass """
}

for filename, initial_code in files.items():
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(initial_code)

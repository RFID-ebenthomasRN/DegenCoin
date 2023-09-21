import logging
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import numpy as np
from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.models import load_model
from keras.optimizers import Adam
import sqlite3

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")


class ModelBuilder:
    @staticmethod
    def build_model():
        model = Sequential()
        model.add(LSTM(units=50, input_shape=(None, 1)))
        model.add(Dense(units=1, activation='sigmoid'))
        opt = Adam(learning_rate=0.01)
        model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
        return model


class FlipPredictor:
    def __init__(self):
        self.history = []
        self.flips = []
        self.predictions = []
        self.model = ModelBuilder.build_model()
        self._connect_db()

    def _connect_db(self):
        self.conn = sqlite3.connect('coinflips.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS coinflips (flip INTEGER)')

    def save_flips(self):
        self.cursor.executemany('INSERT INTO coinflips VALUES (?)', ((flip,) for flip in self.flips))
        self.conn.commit()

    def load_flips(self):
        self.cursor.execute('SELECT flip FROM coinflips')
        self.flips = [flip[0] for flip in self.cursor.fetchall()]

    def close_db(self):
        self.conn.close()

    def update_flips(self, new_flip):
        self.flips.append(new_flip)
        self.cursor.execute('INSERT INTO coinflips VALUES (?)', (new_flip,))
        self.conn.commit()

    def train_lstm(self, x):
        x_train_lstm = np.asarray(x[:-1]).reshape(1, len(x[:-1]), 1)
        y_train_lstm = np.asarray(x[-1:]).reshape(1, 1)
        self.model.fit(x_train_lstm, y_train_lstm, epochs=3)

    def flip(self, outcome):
        flip = 0 if outcome == 'Heads' else 1
        self.history.append(flip)
        self.update_flips(flip)
        if len(self.flips) > 20:
            self.train_lstm(self.flips[-20:])
            self.predict_next_flip_lstm()

    def predict_next_flip_lstm(self):
        self.predictions.append(self.model.predict(np.asarray(self.flips[-20:]).reshape(1, 20, 1)).round())
        return self.predictions[-1]


class App:
    def __init__(self, root):
        self.root = root
        self.predictor = FlipPredictor()
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.var = tk.StringVar()
        self.var.set('Heads')

        self.rd1 = tk.Radiobutton(self.frame, text='Heads', variable=self.var, value='Heads')
        self.rd1.pack(side='left')
        self.rd2 = tk.Radiobutton(self.frame, text='Tails', variable=self.var, value='Tails')
        self.rd2.pack(side='left')
        self.button = tk.Button(root, text='Submit', command=self.flip)
        self.button.pack()
        self.combo = ttk.Combobox(root, textvariable=self.var, values=[100, 200, 300])
        self.combo.pack()
        self.combo.bind('<<ComboboxSelected>>', self.on_combobox_change)

        self.save_button = tk.Button(root, text='Save', command=self.save_model)
        self.save_button.pack()
        self.load_button = tk.Button(root, text='Load', command=self.load_model)
        self.load_button.pack()

    def on_combobox_change(self, _):
        self.predictor.training_threshold = int(self.combo.get())

    def flip(self):
        choice = self.var.get()
        self.predictor.flip(choice)
        last_prediction = self.predictor.predict_next_flip_lstm()
        outcome = 'Heads' if last_prediction == 0 else 'Tails'
        messagebox.showinfo("The prediction is: ", outcome)

    def save_model(self):
        self.predictor.model.save('model.h5')

    def load_model(self):
        self.predictor.model = load_model('model.h5')


def run_app():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    run_app()
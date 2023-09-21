import random
from .model_builder import ModelBuilder
from .game_utils import get_rng_based_on_probability
import numpy as np


class Predictor:
    def predict_next(self):
        raise NotImplementedError


class FrequencyBasedPredictor(Predictor):
    def __init__(self, variables_counts):
        self.variables_counts = variables_counts

    def predict_next(self):
        total_variables = sum(self.variables_counts.values())
        probabilities = [count / total_variables for count in self.variables_counts.values()]
        return list(self.variables_counts.keys())[get_rng_based_on_probability(probabilities)]


class LastOutcomeBasedPredictor(Predictor):
    def __init__(self, last_outcome):
        self.last_outcome = last_outcome

    def predict_next(self):
        return self.last_outcome


class RandomPredictor(Predictor):
    def __init__(self, variables):
        self.variables = variables

    def predict_next(self):
        return random.choice(self.variables)


class LSTMBasedPredictor(Predictor):
    def __init__(self, last_20_variables):
        self.model = ModelBuilder.build_model()
        self.variables = last_20_variables

    def train_model_with_new_variable(self):
        x_train = np.asarray(self.variables[:-1]).reshape(1, 19, 1)
        y_train = np.asarray(self.variables[-1]).reshape(1, 1)
        self.model.fit(x_train, y_train, epochs=1, verbose=0)

    def predict_next(self):
        self.train_model_with_new_variable()
        return self.model.predict(np.asarray(self.variables).reshape(1, 20, 1))
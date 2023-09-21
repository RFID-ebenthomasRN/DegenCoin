from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam


class ModelBuilder:

    @staticmethod
    def build_model():
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(None, 1)))
        model.add(Dense(units=1, activation='sigmoid'))
        opt = Adam(learning_rate=0.01)
        model.compile(loss='binary_crossentropy', optimizer=opt)
        return model
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, Dropout
import matplotlib.pyplot as plt

class RnnModel :
    def __init__(self, step) :
        self.step = step
        self.model = self._createRnnModel()

    def _createRnnModel(self) :
        model = Sequential()

        model.add(SimpleRNN(units=64, input_shape=(1, self.step), activation="relu"))
        model.add(Dense(16, activation="relu"))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.compile(loss="mean_squared_error", optimizer="rmsprop")

        return model

    def trainModel(self, data) :
        data = np.array(data)
        data /= max(data)
        dataX, dataY = self._createDataSet(data)
        self.model.fit(dataX, dataY, epochs=300, batch_size=16, verbose=2)

    def testModel(self, data) :
        maxData = max(data)
        data = np.array(data)
        norData = data/maxData
        dataX, _ = self._createDataSet(norData)

        result = self.model.predict(dataX)
        result *= maxData

        plt.plot(data[self.step:], "-b", result, "-r")
        plt.show()

    def predictModel(self, data, nextDay) :
        savedData = data
        data = np.array(data)

        for i in range(nextDay) :
            maxData = max(data)

            norData = data/maxData
            dataX, _ = self._createDataSet(norData)

            result = self.model.predict(dataX)
            result *= maxData
            data = np.append(data, result[-1])

        plt.plot(savedData[self.step:], "-b", result, "-r")
        plt.show()

    def _createDataSet(self, data) :
        dataX = []
        dataY = []
        for i in range(len(data)-self.step) :
            dataX.append(data[i:i+self.step])
            dataY.append(data[i+self.step])
        dataX = np.array(dataX)
        dataX = dataX.reshape(dataX.shape[0], 1, dataX.shape[1])
        dataY = np.array(dataY)

        return dataX, dataY

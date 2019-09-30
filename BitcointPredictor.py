import LoadTrainingData
import RnnModel

if __name__ == "__main__":
    dataSet = LoadTrainingData.LoadTrainingData().getData()
    model = RnnModel.RnnModel(4)
    model.trainModel(dataSet)
    model.predictModel(dataSet, 365)

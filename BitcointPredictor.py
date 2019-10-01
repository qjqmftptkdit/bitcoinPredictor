import LoadTrainingData
import RnnModel

if __name__ == "__main__":
    dataSet = LoadTrainingData.LoadTrainingData().getData()
    model = RnnModel.RnnModel(4)
    model.predictModel(dataSet, 100)
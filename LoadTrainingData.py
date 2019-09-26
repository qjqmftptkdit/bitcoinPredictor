import requests, json, datetime

class LoadTrainingData :
    def __init__(self) :
        self.apiPath = "https://api.coindesk.com/v1/bpi/historical/close.json"
        self.dayAgo = 365*3

    def getData(self) :
        startDay = self._getPastDay(self.dayAgo)
        apiData = self._loadDataFromApi(self.apiPath, startDay)
        return self._parseData(apiData)

    def _getPastDay(self, dayAgo) :
        pastday = datetime.date.today()-datetime.timedelta(dayAgo)
        return pastday.strftime("%Y-%m-%d")

    def _loadDataFromApi(self, apiPath, startDate) :
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return requests.get("{}?start={}&end={}".format(apiPath, startDate, today))

    def _parseData(self, data) :
        priceValues = json.loads(data.text)["bpi"].values()
        priceList = []
        for price in priceValues :
            priceList.append(price)
        return priceList

if __name__ == "__main__":
    print(LoadTrainingData().getData())


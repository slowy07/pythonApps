import json


class jsonParser:
    def convertJsonToPython(self, parJsonFile):
        with open(parJsonFile) as jsonFile:
            dataDic = json.load(jsonFile)

        return dataDic

    def convertPythonToJson(self, parDataDic, parJsonFile=""):

        if parJsonFile:
            with open(parJsonFile, "w") as outFile:
                return json.dump(parDataDic, outFile)
        else:
            return json.dump(parDataDic)  # lgtm [py/call/wrong-arguments]

    def getJsonValue(self, parValue, parJsonFile):
        dataDic = self.convertJsonToPython(parJsonFile)

        return dataDic[parValue]

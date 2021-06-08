import json

class DataHandler():

    def writeData(self,data,fileDir='\config.json'):
        with open(fileDir,'r') as configfile:
            json.dump(data,configfile,indent=2)
               

    def saveNew(self,fileDir,data):
        with open(fileDir,'r') as configfile:
            json.dump(data,configfile,indent=2)
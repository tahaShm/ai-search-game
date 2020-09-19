import configs

class InputReader:
    
    def __init__(self, fileAddress):

        self.bonusesVal = dict()
        self.readFile(fileAddress)

    def readFile(self, fileAddress):
        with open(fileAddress) as inFile:
            lines = inFile.readlines()

            self.mapSize = self.getPositionFromStr(lines[0])
            self.snakePrimaryPosition = tuple([self.getPositionFromStr(lines[1])])
            self.bonusesNum = int(lines[2][:-1])

            self.bounuses = list()

            for i in range(self.bonusesNum):
                self.fetchBonuses(lines[3 + i])
            self.bounuses = tuple(self.bounuses)

    def getPositionFromStr(self, text):
        splitedText = text.split(',')
        return tuple([int(splitedText[0]), int(splitedText[1][:-1])])

    def fetchBonuses(self, text):
        splitedText = text.split(',')
        result = tuple([int(splitedText[0]), int(splitedText[1])])
        self.bounuses.append(result)
        if int(splitedText[2][:-1]) == 2:
            self.bounuses.append(result)
        return
        
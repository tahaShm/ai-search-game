import configs

class InputReader:
    
    def __init__(self, fileAddress):

        self.bonusesVal = dict()
        self.readFile(fileAddress)

    def readFile(self, fileAddress):
        with open(fileAddress) as inFile:
            lines = inFile.readlines()

            self.mapSize = self.getPositionFromStr(lines[0], 2)
            self.snakePrimaryPosition = tuple([self.getPositionFromStr(lines[1], 2)])
            self.bonusesNum = int(lines[2][:-1])

            self.bounuses = set()

            for i in range(self.bonusesNum):
                self.bounuses.add(self.getPositionFromStr(lines[3 + i], 3))
            self.bounuses = tuple(self.bounuses)

    def getPositionFromStr(self, text, partsNumber):
        splitedText = text.split(',')
        result = None
        if partsNumber == 2:
            result = tuple([int(splitedText[0]), int(splitedText[1][:-1])])
        elif partsNumber == 3:
            result = tuple([int(splitedText[0]), int(splitedText[1])])
            self.bonusesVal[result] = int(splitedText[2][:-1])
        return result
        
import constants

class State:

    def __init__(self, snakePosition, bonusesPosition, maxRow, maxCol, bonusEated = False):
        self.snakePosition = snakePosition
        self.bonusesPosition = bonusesPosition
        self.maxRow = maxRow
        self.maxCol = maxCol

        self.bonusEated = bonusEated

    def __copy__(self):
        return State(self.snakePosition, self.bonusesPosition, self.maxRow, self.maxCol, self.bonusEated)

    def __eq__(self, otherClass):
        if self.snakePosition != otherClass.snakePosition:
            return False
        if self.bonusesPosition != otherClass.bonusesPosition:
            return False
        if self.bonusEated != otherClass.bonusEated:
            return False
        return True

    def __hash__(self):
        return hash((self.snakePosition, self.bonusesPosition))

    def getAvailableActions(self):
        availableActions = set([constants.UP, constants.DOWN, constants.RIGHT, constants.LEFT])
        snakeHead = self.snakePosition[0]
        tempSnakePos = tuple(self.snakePosition)

        if self.bonusEated == False and len(self.snakePosition) > 2:
            tempSnakePos = tempSnakePos[:-1]

        if ((snakeHead[0] + 1) % self.maxRow, snakeHead[1]) in tempSnakePos:
            availableActions.remove(constants.DOWN)

        if ((snakeHead[0] - 1) % self.maxRow, snakeHead[1]) in tempSnakePos:
            availableActions.remove(constants.UP)

        if (snakeHead[0], (snakeHead[1] + 1) % self.maxCol) in tempSnakePos:
            availableActions.remove(constants.RIGHT)

        if (snakeHead[0], (snakeHead[1] - 1) % self.maxCol) in tempSnakePos:
            availableActions.remove(constants.LEFT)

        return availableActions      

    def doAction(self, action):
        snakeHead = self.snakePosition[0]
        newHead = None
        if self.bonusEated == False:
            self.snakePosition = self.snakePosition[:-1]
        if action == constants.UP:
            newHead = (((snakeHead[0] - 1) % self.maxRow, snakeHead[1]), )
        elif action == constants.DOWN:
            newHead = (((snakeHead[0] + 1) % self.maxRow, snakeHead[1]), )
        elif action == constants.RIGHT:
            newHead = ((snakeHead[0], (snakeHead[1] + 1) % self.maxCol), )
        elif action == constants.LEFT:
            newHead = ((snakeHead[0], (snakeHead[1] - 1) % self.maxCol), )

        self.snakePosition = newHead + self.snakePosition
        self.eatBonus(newHead[0])

    def eatBonus(self, location):
        for i in range(len(self.bonusesPosition)):
            if self.bonusesPosition[i] == location:
                self.bonusEated = True
                self.bonusesPosition = self.bonusesPosition[0:i] + self.bonusesPosition[i+1:]
                return
        self.bonusEated = False

    def checkIsGoal(self):
        return len(self.bonusesPosition) == 0
    
    def getClosestBonusDistance(self) : 
        minDistance = constants.BIGNUM
        snakeHead = self.snakePosition[0]
        for bouns in self.bonusesPosition : 
            dx = min(abs(snakeHead[0] - bouns[0]), abs(snakeHead[0] - bouns[0] + self.maxRow), abs(snakeHead[0] - bouns[0] - self.maxRow))
            dy = min(abs(snakeHead[1] - bouns[1]), abs(snakeHead[1] - bouns[1] + self.maxCol), abs(snakeHead[1] - bouns[1] - self.maxCol))
            
            if (dx + dy < minDistance) : 
                minDistance = dx + dy
        return minDistance      

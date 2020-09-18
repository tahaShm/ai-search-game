import constants

class State:

    def __init__(self, snakePosition, bonusesPosition):
        self.snakePosition = snakePosition # Change to tuple
        self.bonusesPosition = bonusesPosition # Change to Tuple

    def __copy__(self):
        return State(self.snakePosition, self.bonusesPosition)

    def __hash__(self):
        hashStr = str(hash(self.snakePosition)) + str(hash(self.bonusesPosition))
        return hash(hashStr)

    def getAvailableActions(self, maxRow, maxCol):
        availableActions = set([constants.UP, constants.DOWN, constants.RIGHT, constants.LEFT])
        snakeHead = self.snakePosition[0]
        if ((snakeHead[0] + 1) % maxRow, snakeHead[1]) in self.snakePosition[:-1]:
            availableActions.remove(constants.DOWN)

        elif ((snakeHead[0] - 1) % maxRow, snakeHead[1]) in self.snakePosition[:-1]:
            availableActions.remove(constants.UP)

        elif (snakeHead[0], (snakeHead[1] + 1) % maxCol) in self.snakePosition[:-1]:
            availableActions.remove(constants.RIGHT)

        elif (snakeHead[0], (snakeHead[1] - 1) % maxCol) in self.snakePosition[:-1]:
            availableActions.remove(constants.LEFT)

        return availableActions

    def doAction(self, action, maxRow, maxCol):
        snakeHead = self.snakePosition[0]
        newHead = None
        self.snakePosition = self.snakePosition[:-1]
        if action == constants.UP:
            newHead = (((snakeHead[0] - 1) % maxRow, snakeHead[1]), )
        elif action == constants.DOWN:
            newHead = (((snakeHead[0] + 1) % maxRow, snakeHead[1]), )
        elif action == constants.RIGHT:
            newHead = ((snakeHead[0], (snakeHead[1] + 1) % maxCol), )
        elif action == constants.LEFT:
            newHead = ((snakeHead[0], (snakeHead[1] - 1) % maxCol), )

        self.snakePosition = newHead + self.snakePosition
        self.eatBonus(newHead[0])

    def eatBonus(self, location):
        for i in range(len(self.bonusesPosition)):
            if self.bonusesPosition[i] == location:
                self.bonusesPosition = self.bonusesPosition[0:i] + self.bonusesPosition[i+1:]
                break

    def checkIsGoal(self):
        return len(self.bonusesPosition) == 0
        
        


# print((-1) % 5)
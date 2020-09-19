from node import implementedQueue

import constants

class BFS:

    def __init__(self, initNode, maxRow, maxCol):
        self.initNode = initNode
        self.resultNode = None
        self.frontier = implementedQueue.Queue()
        self.explored = set()

        self.maxRow = maxRow
        self.maxCol = maxCol

    def run(self):
        self.frontier.add(self.initNode)

        while not self.frontier.isEmpty():
            currNode = self.frontier.get()
            self.explored.add(currNode.state)

            childNode = currNode.createChildNode(3, self.maxRow, self.maxCol)

            for action in currNode.state.getAvailableActions(self.maxRow, self.maxCol):
                childNode = currNode.createChildNode(action, self.maxRow, self.maxCol)

                # if childNode.state in self.explored or self.frontier.contain(childNode):
                #     continue

                if childNode.state.checkIsGoal():
                    print(childNode.state.snakePosition)
                    self.resultNode = childNode
                    return

                self.frontier.add(childNode)

    def printSolution(self):
        print("             BFS pathLength : ", self.resultNode.cost)
        from copy import deepcopy
        node = deepcopy(self.resultNode)
        path = ""
        while(node != None):
            if(node.action == constants.DOWN):
                path += "D"
            elif(node.action == constants.UP):
                path += "U"
            elif(node.action == constants.RIGHT):
                path += "R"
            elif(node.action == constants.LEFT):
                path += "L"
            # print(node.state.bonusEated)
            # print(node.action)
            print(node.state.snakePosition)
            # print(node.state.bonusesPosition)
            # print('.........')
            node = node.parent
        print("             Result path : ", path[::-1], "\n")

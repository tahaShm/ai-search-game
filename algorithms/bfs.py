import time

from node import implementedQueue

import constants

class BFS:

    def __init__(self, initNode, maxRow, maxCol):
        self.initNode = initNode
        self.resultNode = None
        self.frontier = implementedQueue.Queue()

        self.numOfExploredStates = 0
        self.numOfUniqueExploredStates = 0

        self.explored = set()

        self.maxRow = maxRow
        self.maxCol = maxCol

    def run(self):
        startTime = time.time()
        self.frontier.add(self.initNode)
        self.numOfExploredStates += 1
        self.numOfUniqueExploredStates += 1
        # print('INIT HASH:')
        # print(hash(self.initNode))

        while not self.frontier.isEmpty():
            currNode = self.frontier.get()
            self.explored.add(currNode.state)

            for action in currNode.state.getAvailableActions(self.maxRow, self.maxCol):
                childNode = currNode.createChildNode(action, self.maxRow, self.maxCol)
                self.numOfExploredStates += 1

                tt = time.time()
                if childNode.state in self.explored or self.frontier.contain(childNode):
                    continue
                self.optimizeCode = time.time() - tt

                self.numOfUniqueExploredStates += 1

                if childNode.state.checkIsGoal():
                    self.execTime = time.time() - startTime
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
            node = node.parent
        print("             Result path : ", path[::-1], "\n")
        print(self.numOfUniqueExploredStates)
        print(self.numOfExploredStates)
        print(self.execTime)
        print(self.optimizeCode)

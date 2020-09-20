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

        self.time1 = 0
        self.time2 = 0
        self.time3 = 0
        self.time4 = 0


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
                t1 = time.time()
                childNode = currNode.createChildNode(action, self.maxRow, self.maxCol)
                self.numOfExploredStates += 1
                self.time1 += time.time() - t1

                t2 = time.time()
                if childNode.state in self.explored or self.frontier.contain(childNode):
                    continue
                self.time2 += time.time() - t2

                self.numOfUniqueExploredStates += 1

                t3 = time.time()
                if childNode.state.checkIsGoal():
                    self.execTime = time.time() - startTime
                    self.resultNode = childNode
                    return
                self.time3 += time.time() - t3

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
        # print(self.time1)
        # print(self.time2)
        # print(self.time3)

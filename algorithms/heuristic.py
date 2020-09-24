import time
from copy import deepcopy

from node import implementedQueue

import constants

class AStar:

    def __init__(self, initNode, hFunction):
        self.initNode = initNode
        self.resultNode = None
        self.frontier = implementedQueue.Queue()

        self.numOfExploredStates = 0
        self.numOfUniqueExploredStates = 0

        self.explored = set()
        
        self.hFunction = hFunction

    def run(self):
        startTime = time.time()
        self.frontier.add(self.initNode)
        self.numOfExploredStates += 1
        self.numOfUniqueExploredStates += 1

        while not self.frontier.isEmpty():
            # print (self.numOfExploredStates)
            currNode = self.frontier.getBest()
            self.explored.add(currNode.state)

            for action in currNode.state.getAvailableActions():
                childNode = currNode.createChildNode(action, self.hFunction)
                self.numOfExploredStates += 1

                if childNode.state in self.explored or self.frontier.contain(childNode):
                    continue

                self.numOfUniqueExploredStates += 1

                if childNode.state.checkIsGoal():
                    self.execTime = time.time() - startTime
                    self.resultNode = childNode
                    return

                self.frontier.add(childNode)

    def printSolution(self):
        print("             A* Execution time : ", self.execTime)
        print("             A* pathLength : ", self.resultNode.cost)
        print("             Total states : ", self.numOfExploredStates)
        print("             Total unique states : ", self.numOfUniqueExploredStates)
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

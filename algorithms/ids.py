import time
from copy import deepcopy

import constants

class IDS:

    def __init__(self, initNode, maxRow, maxCol):
        self.initNode = initNode
        self.resultNode = None

        self.numOfExploredStates = 0
        self.numOfUniqueExploredStates = 0

        self.allExplored = set()

        self.maxRow = maxRow
        self.maxCol = maxCol

    def run(self):
        depth = 0
        startTime = time.time()
        self.numOfExploredStates = 1
        while True:
            depth += 1
            result = self.DFS(self.initNode, depth, set(), dict())
            if(result != None):
                break
        self.execTime = time.time() - startTime

    def DFS(self, currNode, depth, explored, stateLevel):
        
        if(depth <= 0):
            return None

        for action in currNode.state.getAvailableActions(self.maxRow, self.maxCol):
            childNode = currNode.createChildNode(action, self.maxRow, self.maxCol)
            
            self.numOfExploredStates += 1

            if childNode.state in explored:
                if(stateLevel[childNode.state] <= childNode.cost):
                    continue

            explored.add(childNode.state)
            stateLevel[childNode.state] = childNode.cost

            if childNode.state not in self.allExplored:
                self.numOfUniqueExploredStates += 1
                self.allExplored.add(childNode.state)

            if childNode.state.checkIsGoal():
                self.resultNode = childNode
                return childNode
            
            res = self.DFS(childNode, depth - 1, explored, stateLevel)
            
            if(res != None):
                return res 
        
        return None

    def printSolution(self):
        print("             IDS Execution time : ", self.execTime)
        print("             IDS pathLength : ", self.resultNode.cost)
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
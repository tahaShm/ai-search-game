class Node:

    def __init__(self, state, parent = None, action = None, cost = 0, h = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.h = h

    def __hash__(self):
        hashStr = str(hash(self.state))
        return hash(hashStr)
    
    def getHeuristic1(self, curState) : 
        return 0
    
    def getHeuristic2(self, curState) : 
        return len(curState.bonusesPosition) + curState.getClosestBonusDistance()
        
    def getHeuristic(self, curState, hFunction) : 
        if (hFunction == 1) : 
            return self.getHeuristic1(curState)
        elif (hFunction == 2) : 
            return self.getHeuristic2(curState)
        else : 
            return 0

    def createChildNode(self, action, hFunction = 0):
        childState = self.state.__copy__()
        childState.doAction(action)
        hf = self.getHeuristic(childState, hFunction)
        return Node(childState, self, action, self.cost + 1, hf)

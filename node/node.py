
class Node:

    def __init__(self, state, parent = None, action = None, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __hash__(self):
        hashStr = str(hash(self.state))
        return hash(hashStr)

    def createChildNode(self, action, maxRow, maxCol):
        childState = self.state.__copy__()
        childState.doAction(action, maxRow, maxCol)
        return Node(childState, self, action, self.cost + 1)

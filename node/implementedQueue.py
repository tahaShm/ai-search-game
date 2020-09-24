import constants

class Queue:
    
    def __init__(self):
        self.queueList = list()
        self.hashList = set()

    def add(self, elem):
        self.queueList.append(elem)
        self.hashList.add(hash(elem))

    def get(self):
        return self.queueList.pop(0)
    
    def getBest(self) : 
        minActFunc = constants.BIGNUM
        i = 0
        counter = 0
        for curNode in self.queueList : 
            if (curNode.cost + curNode.h < minActFunc) : 
                minActFunc = curNode.cost + curNode.h
                i = counter
            counter += 1
        return self.queueList.pop(i)

    def isEmpty(self):
        return len(self.queueList) == 0

    def contain(self, element):
        return hash(element) in self.hashList
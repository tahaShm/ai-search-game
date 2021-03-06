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
    
    def isEmpty(self):
        return len(self.queueList) == 0

    def contain(self, element):
        return hash(element) in self.hashList
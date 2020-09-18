
class Queue:
    
    def __init__(self):
        self.queueList = list()
        self.hashList = list()

    def add(self, elem):
        self.queueList.append(elem)
        self.hashList.append(hash(elem))

    def get(self):
        self.hashList.pop(0)
        return self.queueList.pop(0)


    def isEmpty(self):
        return len(self.queueList) == 0

    def contain(self, element):
        return hash(element) in self.hashList
import constants
import heapq

class PQueue:
    
    def __init__(self):
        self.pQueueList = list()
        self.hashList = set()

    def add(self, elem):
        heapq.heappush(self.pQueueList, [elem.cost + elem.h, hash(elem),  elem])
        self.hashList.add(hash(elem))

    def get(self):
        return heapq.heappop(self.pQueueList)

    def isEmpty(self):
        return len(self.pQueueList) == 0

    def contain(self, element):
        return hash(element) in self.hashList
class Queue:
    
    def __init__(self):
        self.queueList = list()
        # self.hashList = list()
        self.hashList = set()

    def add(self, elem):
        self.queueList.append(elem)
        # self.hashList.append(hash(elem))
        self.hashList.add(hash(elem))

    def get(self):
        # self.hashList.pop(0)
        return self.queueList.pop(0)


    def isEmpty(self):
        return len(self.queueList) == 0

    def contain(self, element):
        # return hash(element) in self.hashList

        return hash(element) in self.hashList







# class Queue:
    
#     def __init__(self):
#         self.queueList = list()
#         self.hashList = set()

#     def add(self, elem):
#         self.queueList.append(elem)
#         # self.hashList.append(hash(elem))
#         self.hashList.add(elem)

#     def get(self):
#         tempElem = self.queueList.pop(0)
#         self.hashList.remove(tempElem)
#         return tempElem


#     def isEmpty(self):
#         return len(self.queueList) == 0

#     def contain(self, element):
#         # return hash(element) in self.hashList
#         return element in self.hashList
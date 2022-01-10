import math
class FrontMiddleBackQueue(object):

    def __init__(self):
        self.list = []
        idx = 0

    def pushFront(self, val):
        self.list.insert(0, val)
        

    def pushMiddle(self, val):
        idx = math.floor(len(self.list)/2)
        self.list.insert(int(idx), val)
        

    def pushBack(self, val):
        self.list.append(val)
        

    def popFront(self):
        if len(self.list) == 0:
            return -1
        return self.list.pop(0)
        

    def popMiddle(self):
        if len(self.list) == 0:
            return -1
        else:
            if len(self.list)%2 == 0:
                idx = len(self.list)/2 - 1
                return self.list.pop(int(idx))
            else:
                idx = len(self.list)/2
                return self.list.pop(int(idx))
            
        
    def popBack(self):
        if len(self.list) == 0:
            return -1
        return self.list.pop(-1)
class MinStack:
    
    def __init__(self):
        self.list = []
        
    def push(self, val):
        self.list.append(val)
        
    def pop(self):
        if len(self.list) > 0:
            return self.list.pop()
        else:
            return -1

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return -1
        
    def getMin(self):
        if len(self.list) > 0:
            return min(self.list)
        else:
            return -1
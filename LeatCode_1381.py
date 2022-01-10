class CustomStack(object):
    
    def __init__(self, maxSize):
        self.maxsize = maxSize
        self.list = []

    def push(self, x):
        if len(self.list) < self.maxsize:
            self.list.append(x)
        else:
            print("Stack is Full")

    def pop(self):
        if len(self.list) == 0:
            return -1
        else:
            return self.list.pop()

    def increment(self, k, val):
        if k < self.maxsize:
            for i in range(k):
                self.list[i] += val
        else:
            for i in range(self.maxsize):
                self.list[i] += val
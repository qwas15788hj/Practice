class Solution(object):
    def finalValueAfterOperations(self, operations):
        self.operations = operations
        x = 0
        
        for i in range(len(self.operations)):
            if self.operations[i][1] == '+':
                x += 1
            else:
                x -= 1
        
        return x
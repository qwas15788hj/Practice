class Solution(object):
    def addBinary(self, a, b):
        x = int(a,2) + int(b,2)
        
        return bin(x)[2:]
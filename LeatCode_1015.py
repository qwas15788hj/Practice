class Solution(object):
    def smallestRepunitDivByK(self, k):
        self.k = k
        n = 0
        
        if self.k%2 == 0 or self.k%5 == 0:
            return -1
        
        else:
            for i in range(self.k):
                n = (n*10+1)%self.k
                if n == 0:
                    return i+1
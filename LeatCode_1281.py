class Solution(object):
    def subtractProductAndSum(self, n):
        a = list(map(int, str(n)))
        
        x = 1
        for i in range(len(a)):
            x *= a[i]
            
        return x-sum(a)
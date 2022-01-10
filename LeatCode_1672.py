class Solution(object):
    def maximumWealth(self, accounts):
        a = accounts
        result = 0
        rich = 0
        
        for i in range(len(a)):
            result = 0
            for j in range(len(a[i])):
                result += a[i][j]
                
            if rich < result:
                rich = result
                
        return rich
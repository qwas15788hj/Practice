class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        a = jewels
        b = stones
        count = 0
        
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    count += 1
        
        return count
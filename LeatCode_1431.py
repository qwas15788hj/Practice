class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a = candies
        b = extraCandies
        list = []
        
        for i in range(len(a)):
            if a[i] + b < max(a):
                list.append(False)
            else:
                list.append(True)
            
        return list
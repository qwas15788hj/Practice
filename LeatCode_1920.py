class Solution(object):
    def buildArray(self, nums):
        self.nums = nums
        self.output = []
        
        for i in range(len(self.nums)):
            self.output.append(self.nums[self.nums[i]])
            
        return self.output
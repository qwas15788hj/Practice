class Solution(object):
    def runningSum(self, nums):
        self.nums = nums
        a = 0
        self.output = []
        
        for i in range(len(self.nums)):
            a = a + self.nums[i]
            self.output.append(a)
            
        return self.output
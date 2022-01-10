class Solution(object):
    def getConcatenation(self, nums):
        self.nums = nums
        self.output = []
        
        for i in range(len(self.nums)*2):
            self.output.append(self.nums[i%len(self.nums)])
            
        return self.output
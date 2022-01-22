class Solution(object):
    def decompressRLElist(self, nums):
        result = []
        for i in range(len(nums)/2):
            for j in range(nums[2*i]):
                result.append(nums[2*i+1])
                
        return result
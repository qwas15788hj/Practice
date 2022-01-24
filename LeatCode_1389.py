class Solution(object):
    def createTargetArray(self, nums, index):
        list = []
        for i in range(len(nums)):
            if i == index[i]:
                list.append(nums[i])
            else:
                list.insert(index[i], nums[i])
        
        return list
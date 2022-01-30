class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            a = nums[-1]
            for j in range(len(nums)-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = a

        print(nums)
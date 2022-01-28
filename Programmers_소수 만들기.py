def solution(nums):
    count = 0
    a = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for z in range(j+1, len(nums)):
                if nums[i] != nums[j] and nums[i] != nums[z] and nums[j] != nums[z]:
                    a = nums[i] + nums[j] + nums[z]
                    temp = 0
                    for r in range(2, a):
                        if a % r == 0:
                            temp = 1
                            break
                    
                    if temp == 0:
                        count += 1
    
    return count
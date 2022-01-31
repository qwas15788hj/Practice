def solution(nums):
    num = list(set(nums))
    if len(num) > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(num)
    return answer
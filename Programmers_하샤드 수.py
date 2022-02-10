def solution(x):
    answer = False
    num = list(map(int, str(x)))
    
    if x%sum(num) == 0:
        answer = True
        return answer
    
    return answer
def solution(numbers):
    result = [0]*10
    answer = 0
    for i in range(len(numbers)):
        result[numbers[i]] += 1
    
    for i in range(len(result)):
        if result[i] == 0:
            answer += i
            
    return answer
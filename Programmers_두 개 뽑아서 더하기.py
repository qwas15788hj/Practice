def solution(numbers):
    num = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            num.append(numbers[i] + numbers[j])
    
    answer = list(set(num))
    answer.sort()
    return answer
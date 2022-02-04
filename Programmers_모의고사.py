def solution(answers):
    list_1 = [1,2,3,4,5]
    list_2 = [2,1,2,3,2,4,2,5]
    list_3 = [3,3,1,1,2,2,4,4,5,5]
    result = []
    
    count = 0
    for i in range(len(answers)):
        if answers[i] == list_1[i%5]:
            count += 1
    result.append(count)
    
    count = 0
    for i in range(len(answers)):
        if answers[i] == list_2[i%8]:
            count += 1
    result.append(count)
    
    count = 0
    for i in range(len(answers)):
        if answers[i] == list_3[i%10]:
            count += 1
    result.append(count)
    
    max_score = max(result)
    answer = []
    for i in range(len(result)):
        if result[i] == max_score:
            answer.append(i+1)
    
    return answer
def solution(N, stages):
    num = len(stages)
    stage_list = [0]*(N+1)
    answer = []
    
    for i in range(len(stages)):
        stage_list[stages[i]-1] += 1
        
    for i in range(len(stage_list)):
        person = stage_list[i]
        if person == 0:
            stage_list[i] = 0
        else:
            stage_list[i] = stage_list[i]/num
            num = num-person

    stage_list.pop()
    
    for i in range(len(stage_list)):
        max_index = stage_list.index(max(stage_list))
        stage_list[max_index] = -1
        answer.append(max_index+1)
    
    return answer
def solution(progresses, speeds):
    answer = []
    day = [] # 몇 일 걸렸는지
    
    # progresses수 만큼 돌리기
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        day.append(count)
    print(day) # [7,3,9]

    # 스택 day가 빌 때까지
    max_day = 0
    while len(day) != 0:
        if max_day < day[0]:
            max_day = day[0]
        day.pop(0)
        answer.append(max_day) # [7,7,9]
    
    # 카운트 세주기
    max_time = 0
    result = []
    cnt = 0
    for i in range(len(answer)):
        if max_time < answer[i]: # max_time보다 큰 값이 들어오면
            max_time = answer[i] # max_time 바꿔주고
            result.append(cnt) # result에 카운트 넣어주고
            cnt = 1 # 카운트 1로 초기화
        else:
            cnt += 1 # max_time보다 작은 값이 들어오면 카운트만 1 증가
            
    result.append(cnt) # 마지막 카운트가 들어오지않기 때문에 마지막 카운트 넣어주는 예외처리
    result.pop(0) # 처음에 빈 카운트인 0을 넣고 시작하기에 처음 카운트를 없애주는 예외처리

    return result
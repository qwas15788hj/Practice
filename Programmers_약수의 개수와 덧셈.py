def solution(left, right):
    answer = 0
    for i in range(left, right+1): # 13, 14, 15 하나씩
        count = 0
        for j in range(1, i+1): # 13을 1~13까지
            if i%j == 0: # 0 이면 카운트
                count += 1
        if count%2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer
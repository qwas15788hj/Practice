def solution(x, n):
    answer = []
    # 음수일 때
    if x < 0:
        for i in range(x, x*n-1, x):
            answer.append(i)
    # 양수일 때
    elif x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
    # **중요!** x가 0일 때 => 안해주면 런타임 에러남 
    elif x == 0:
        return [0]*n
    
    return answer
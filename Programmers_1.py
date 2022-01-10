def solution(lottos, win_nums):
    a = lottos
    b = win_nums
    count = 0 # 맞은 수
    zero = 0 # 모르는 수
    
    for i in range(0, 6):
        for j in range(0, 6):
            if a[i] == b[j]:
                count += 1

        if a[i] == 0:
            zero += 1

    c = 7-(count+zero)
    d = 7-count
    
    if c > 6:
        c = 6
    if d > 6:
        d = 6
    
    answer = [c, d]
    return answer
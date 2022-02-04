def solution(n, lost, reserve):
    count = n-len(lost)
    lost.sort()
    reserve.sort()
    
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
            count+=1
    
# ===이건 왜 안되지?? (위에랑 같음)
    # for i in lost:
    #     if i in reserve:
    #         reserve.remove(i)
    #         lost.remove(i)
    #         count += 1

    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            count += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            count += 1

    return count

# 다른 사람 코드==================

def solution(n, lost, reserve):
    # 차집합을 사용하기 위해 set 자료형 사용
    lost_list = set(lost) - set(reserve)
    reserve_list = set(reserve) - set(lost)
    count = n - len(lost_list)
    
    for i in lost_list:
        if i-1 in reserve_list:
            reserve_list.remove(i-1)
            count += 1
        elif i+1 in reserve_list:
            reserve_list.remove(i+1)
            count += 1

    return count
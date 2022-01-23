from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list) # 결과값 리스트
    black_list = [] # 정지먹은사람 리스트
    report = set(report) # 리포트 중복 제거
    
    user_list = defaultdict(set) # 신고한사람 set / muzi:frodo 이렇게 만들거
    user_num = defaultdict(int) # 신고당한사람 카운트 / frodo:2 이렇게 만들거
    
    # 리포트 반복
    for r in report:
        front , back = r.split() # 신고한사람 => front / 신고당한사람 => back
        user_list[front].add(back) # 신고한사람 set / muzi(front):frodo(back)
        user_num[back] += 1 # 신고당한사람 / frodo(back):2
        
        if user_num[back] == k: # user_num[back] => frodo의 int값인 2
            black_list.append(back) # 블랙리스트 추가
    
    for b in black_list: # 블랙리스트만큼 반복
        for i in range(len(id_list)): # 아이디리스트 반복
            if b in user_list[id_list[i]]: # 블랙리스트가 set에 muzi:frodo에서 뒤에 있을때
                answer[i] += 1
    
    return answer
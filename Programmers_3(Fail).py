def solution(id_list, report, k):
    # 중복 제거
    new_report = []
    for i in report:
        if i not in new_report:
            new_report.append(i)
    
    # 누가 얼마나 신고먹었는지 찾기
    list = [0] * len(id_list) # id_list 길이 만큼 빈 리스트 만들기
    for i in range (len(new_report)):
        for j in range(len(id_list)):
            if new_report[i].split()[1] == id_list[j]:
                list[j] += 1
    
    # 정지 먹을 사람 찾기
    name_list = []
    for i in range(len(list)):
        if list[i] >= k:
            name_list.append(id_list[i])
    
    # 정지 먹을 사람이 있는 신고만 찾기
    last_report = [] 
    for i in range(len(new_report)):
        for j in range(len(name_list)):
            if new_report[i].split()[1] == name_list[j]:
                last_report.append(new_report[i])
    
    # 정지 먹을 사람이 있는 신고에서 아이디 찾기
    result = [0] * len(id_list)
    for i in range(len(last_report)):
        for j in range(len(id_list)):
            if last_report[i].split()[0] == id_list[j]:
                result[j] += 1
    
    return result
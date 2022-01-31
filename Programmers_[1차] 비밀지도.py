def solution(n, arr1, arr2):
    list_1 = []
    list_2 = []
    # 이진수로 바꾸고 자리수 맞추기 위해 0 추가
    for i in range(len(arr1)):
        list_1.append(bin(arr1[i])[2:])
        while len(list_1[i]) < n:
            list_1[i] = '0' + list_1[i]
    # 이진수로 바꾸고 자리수 맞추기 위해 0 추가
    for i in range(len(arr2)):
        list_2.append(bin(arr2[i])[2:])
        while len(list_2[i]) < n:
            list_2[i] = '0' + list_2[i]
        
    result = []
    # 두 지도 모두 0 일때만 빈칸
    for i in range(n):
        answer = ""
        for j in range(n):
            if list_1[i][j] == '0' and list_2[i][j] == '0':
                answer += " "
            else:
                answer += "#"
        result.append(answer)

    return result
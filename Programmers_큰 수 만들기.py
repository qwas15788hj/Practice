def solution(number, k):
    answer = ""
    max_index = -1
    
    # number에서 k뺀 만큼 반복
    for i in range(1, len(number)-k+1):
        max_num = 0
        # max_index 다음 ~ 뒤에 꼭 나와야 할 숫자의 개수까지
        for j in range(max_index+1, k+i):
            if max_num < int(number[j]):
                if int(number[j] == '9'): # 9가 가장 크기에 9가 나오면 더 이상 체크 안함
                    max_num = int(number[j]) # 이 부분을 안하면 타임오버됨
                    max_index = j
                    break
                else:
                    max_num = int(number[j])
                    max_index = j
    
        answer += str(max_num)

    return answer
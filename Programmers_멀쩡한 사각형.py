def solution(w,h):
    # w, h 공약수
    div_list = []
    for i in range(1, min(w, h)+1):
        if w%i == 0 and h%i == 0:
            div_list.append(i)

    # w, h 최대공약수
    max_div = max(div_list)
    
    # 가로 세로 공약수로 나눈 몫
    a = w//max_div # 2
    b = h//max_div # 3
    
    # 사라지는 부분은 겹치는 부분에서 2개 됨
    # => 가로+세로-1
    answer = (w*h) - (max_div*(a+b-1))
    return answer
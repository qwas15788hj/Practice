def solution(n):
    answer = ""
    a = list(map(str, str(n)))
    a.sort(reverse=True)
    
    for i in a:
        answer += i

    return int(answer)
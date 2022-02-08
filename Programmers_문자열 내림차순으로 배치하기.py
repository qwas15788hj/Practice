def solution(s):
    result = []
    answer = ""
    for i in s:
        result.append(ord(i))
        
    result.sort(reverse=True)
    
    for i in result:
        answer += chr(i)
        
    return answer
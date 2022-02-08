def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i].isalpha() == True:
                answer = False
                return answer
        answer = True
        return answer
    
    else:
        answer = False
        return answer
def solution(s, n):
    answer = ""
    for i in range(len(s)):
        if s[i].isupper() == True:
            if int(ord(s[i]))+n <= int(ord('Z')):
                answer += chr(int(ord(s[i]))+n)
            else:
                answer += chr(int(ord(s[i]))+n-26)
                
        elif s[i].islower() == True:
            if int(ord(s[i]))+n <= int(ord('z')):
                answer += chr(int(ord(s[i]))+n)
            else:
                answer += chr(int(ord(s[i]))+n-26)    
                
        else:
            answer += " "
        
    return answer
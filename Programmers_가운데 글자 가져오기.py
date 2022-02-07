import math

def solution(s):
    if len(s)%2 == 1:
        return s[math.floor(len(s)/2)]
    else:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
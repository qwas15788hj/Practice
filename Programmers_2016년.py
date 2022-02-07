def solution(a, b):
    a_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    data = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    for i in range(a-1):
        b += a_list[i]
    
    return data[b%7]
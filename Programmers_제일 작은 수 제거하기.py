def solution(arr):
    arr.pop(arr.index(min(arr)))
    if len(arr) < 1:
        arr.append(-1)
    return arr
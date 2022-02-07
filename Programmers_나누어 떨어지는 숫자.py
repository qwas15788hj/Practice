def solution(arr, divisor):
    result = []
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            result.append(arr[i])
    
    if len(result) != 0:
        result.sort()
    else:
        result.append(-1)
    return result
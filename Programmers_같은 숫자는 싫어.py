def solution(arr):
    result = []
    arr.append(-1)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            pass
        else:
            result.append(arr[i])
    return result
def solution(rows, columns, queries):
    answer = []
    # 배열 선언
    arr = [[0]*columns for i in range(rows)]
    a = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = a
            a += 1
            
    # queries 만큼 돌리기
    for q in range(len(queries)):
        result = []
        now = arr[queries[q][0]-1][queries[q][1]-1]
        # 오른쪽
        for j in range(queries[q][1]-1, queries[q][3]-1): # 오른쪽으로 2번 / 1, 2
            arr[queries[q][0]-1][j+1], now = now, arr[queries[q][0]-1][j+1]
            result.append(now)
        # 아래쪽
        for z in range(queries[q][0]-1, queries[q][2]-1): # 아래로 3번 / 1, 2, 3
            arr[z+1][queries[q][3]-1], now = now, arr[z+1][queries[q][3]-1]
            result.append(now)
        # 왼쪽
        for l in range(queries[q][3]-1, queries[q][1]-1, -1): # 왼쪽으로 2번 / 3, 2
            arr[queries[q][2]-1][l-1], now = now, arr[queries[q][2]-1][l-1]
            result.append(now)
        # 위쪽
        for u in range(queries[q][2]-1, queries[q][0]-1, -1): # 위쪽으로 3번
            arr[u-1][queries[q][1]-1], now = now, arr[u-1][queries[q][1]-1]
            result.append(now)
            
        answer.append(min(result))
    return answer
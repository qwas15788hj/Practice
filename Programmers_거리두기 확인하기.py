def solution(places):
    answer = []
    for place in places:
        err = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if j+1 < 5 and place[i][j+1] == 'P': # 오른쪽 1칸
                        err += 1
                        break
                    elif j-1 > -1 and place[i][j-1] == 'P': # 왼쪽 1칸
                        err += 1
                        break
                    elif i-1 > -1 and place[i-1][j] == 'P': # 위로 1칸
                        err += 1
                        break
                    elif i+1 < 5 and place[i+1][j] == 'P': # 아래로 1칸
                        err += 1
                        break
                    # 오른쪽 위
                    elif i-1 > -1 and j+1 < 5 and place[i-1][j+1] == 'P' and (place[i-1][j] == 'O' or place[i][j+1] == 'O'):
                        err += 1
                        break
                    # 오른쪽 아래
                    elif i+1 < 5 and j+1 < 5 and place[i+1][j+1] == 'P' and (place[i+1][j] == 'O' or place[i][j+1] == 'O'):
                        err += 1
                        break
                    # 왼쪽 위
                    elif i-1 > -1 and j-1 > -1 and place[i-1][j-1] == 'P' and (place[i-1][j] == 'O' or place[i][j-1] == 'O'):
                        err += 1
                        break
                    # 왼쪽 아래
                    elif i+1 < 5 and j-1 > -1 and place[i+1][j-1] == 'P' and (place[i+1][j] == 'O' or place[i][j-1] == 'O'):
                        err += 1
                        break
                    elif j+2 < 5 and place[i][j+2] == 'P' and place[i][j+1] == 'O': # 오른쪽 2칸
                        err += 1
                        break
                    elif j-2 > -1 and place[i][j-2] == 'P' and place[i][j-1] == 'O': # 왼쪽 2칸
                        err += 1
                        break
                    elif i-2 > -1 and place[i-2][j] == 'P' and place[i-1][j] == 'O': # 위로 2칸
                        err += 1
                        break
                    elif i+2 < 5 and place[i+2][j] == 'P' and place[i+1][j] == 'O': # 아래로 2칸
                        err += 1
                        break

            if err > 0:
                answer.append(0)
                break
        if err == 0:
            answer.append(1)
    
    return answer
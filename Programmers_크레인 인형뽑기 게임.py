def solution(board, moves):
    stack = []
    count = 0
    
    for i in range(len(moves)):
        if board[len(board)-1][moves[i]-1] == 0: # 마지막 끝이 0이면 => 빈 열이면 pass
            pass
        else:
            j = 0
            while board[j][moves[i]-1] == 0: # 해당 열(moves[i]-1) 중 0이 아닌 열 찾기
                j += 1
            stack.append(board[j][moves[i]-1]) # 찾았으면 stack에 넣기
            board[j][moves[i]-1] = 0 # 넣었으면 해당 부분 0 처리
            
            if len(stack) > 1 and stack[-1] == stack[-2]: # 스택이 2이상이고 앞뒤가 같으면
                stack.pop()
                stack.pop()
                count += 2
    
    return count
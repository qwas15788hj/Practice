# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    array = [[1,2,3],[4,5,6],[7,8,9],['*',0,"#"]]
    left_hand = [3,0]
    right_hand = [3,2]
    answer = ""

    for i in range(len(numbers)):
        if numbers[i] == 1:
            answer += "L"
            left_hand = [0,0]
            
        elif numbers[i] == 4:
            answer += "L"
            left_hand = [1,0]
            
        elif numbers[i] == 7:
            answer += "L"
            left_hand = [2,0]
            
        elif numbers[i] == 3:
            answer += "R"
            right_hand = [0,2]
            
        elif numbers[i] == 6:
            answer += "R"
            right_hand = [1,2]
            
        elif numbers[i] == 9:
            answer += "R"
            right_hand = [2,2]
            
        elif numbers[i] == 2:
            if abs(0-left_hand[0])+abs(1-left_hand[1]) < abs(0-right_hand[0])+abs(1-right_hand[1]):
                answer += "L"
                left_hand = [0,1]
            elif abs(0-left_hand[0])+abs(1-left_hand[1]) > abs(0-right_hand[0])+abs(1-right_hand[1]):
                answer += "R"
                right_hand = [0,1]
            elif abs(0-left_hand[0])+abs(1-left_hand[1]) == abs(0-right_hand[0])+abs(1-right_hand[1]):
                if hand == "right":
                    answer += "R"
                    right_hand = [0,1]
                else:
                    answer += "L"
                    left_hand = [0,1]

        elif numbers[i] == 5:
            if abs(1-left_hand[0])+abs(1-left_hand[1]) < abs(1-right_hand[0])+abs(1-right_hand[1]):
                answer += "L"
                left_hand = [1,1]
            elif abs(1-left_hand[0])+abs(1-left_hand[1]) > abs(1-right_hand[0])+abs(1-right_hand[1]):
                answer += "R"
                right_hand = [1,1]
            elif abs(1-left_hand[0])+abs(1-left_hand[1]) == abs(1-right_hand[0])+abs(1-right_hand[1]):
                if hand == "right":
                    answer += "R"
                    right_hand = [1,1]
                else:
                    answer += "L"
                    left_hand = [1,1]
                
        elif numbers[i] == 8:
            if abs(2-left_hand[0])+abs(1-left_hand[1]) < abs(2-right_hand[0])+abs(1-right_hand[1]):
                answer += "L"
                left_hand = [2,1]
            elif abs(2-left_hand[0])+abs(1-left_hand[1]) > abs(2-right_hand[0])+abs(1-right_hand[1]):
                answer += "R"
                right_hand = [2,1]
            elif abs(2-left_hand[0])+abs(1-left_hand[1]) == abs(2-right_hand[0])+abs(1-right_hand[1]):
                if hand == "right":
                    answer += "R"
                    right_hand = [2,1]
                else:
                    answer += "L"
                    left_hand = [2,1]
                    
        elif numbers[i] == 0:
            if abs(3-left_hand[0])+abs(1-left_hand[1]) < abs(3-right_hand[0])+abs(1-right_hand[1]):
                answer += "L"
                left_hand = [3,1]
            elif abs(3-left_hand[0])+abs(1-left_hand[1]) > abs(3-right_hand[0])+abs(1-right_hand[1]):
                answer += "R"
                right_hand = [3,1]
            elif abs(3-left_hand[0])+abs(1-left_hand[1]) == abs(3-right_hand[0])+abs(1-right_hand[1]):
                if hand == "right":
                    answer += "R"
                    right_hand = [3,1]
                else:
                    answer += "L"
                    left_hand = [3,1]
                    
    return answer
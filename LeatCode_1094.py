class Solution(object):
    def carPooling(self, trips, capacity):
        a = trips
        b = capacity
        answer = True
        list = []
        maxsize = 0
        
        
        if len(a) == 0:
            return answer
        
        elif len(a) == 1:
            if a[0][0] > b:
                answer = False
                return answer
            return answer
                
            
        elif len(a) > 1:
            # 리스트를 만들기 위해 제일 긴 길이 찾기
            for i in range(len(a)):
                if a[i][2] > maxsize:
                    maxsize = a[i][2]
                    
            # 0도 있으니 +1 해서 리스트 만듬
            for i in range(maxsize+1):
                list.append([i,0])

            # 리스트 하나마다 돌리기
            for i in range(len(a)):
                result = 0
                # 하나씩해서 차를 탈때 result 증가 내릴때 result 감소
                for j in range(maxsize+1):
                    if a[i][1] != a[i][2]:
                        if a[i][1] == j:
                            result += a[i][0]
                        elif a[i][2] == j:
                            result -= a[i][0]
                        
                        # 리스트에 result 더해서 삽입
                        list[j][1] = list[j][1]+result

            # 리스트 돌려서 하나라도 cap보다 크면 false
            for i in range(len(list)):
                if list[i][1] > b:
                    answer = False
                    return answer

            return answer
class Solution(object):
    def addDigits(self, num):        
        num = str(num)
        
        if len(num) == 1:
            return int(num)
        else:
            while len(num) > 1:
                answer = 0
                for i in range(len(num)):
                    answer += int(num[i])
                num = str(answer)

            return answer
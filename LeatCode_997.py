class Solution(object):
    def findJudge(self, n, trust):
        n = n
        trust = trust
        cnt = 0
        a = 0
        list = []
        result_list = []
        
        if n == 1:
            return n
        
        elif n-1 > len(trust):
            return -1
        
        elif n-1 == len(trust):
            for i in range(len(trust)):
                if trust[0][1] != trust[i][1]:
                    return -1
                else:
                    a = trust[0][1]
            return a
                    
        
        elif n-1 < len(trust):
            for i in range(len(trust)):
                cnt = 0
                for j in range(len(trust)):
                    if trust[i][1] == trust[j][1]:
                        cnt += 1
                    if trust[i][1] == trust[j][0]:
                        cnt -= 1
                        
                if cnt == n-1:
                    list.append(trust[i][1])
                    

            for value in list:
                if value not in result_list:
                    result_list.append(value)
            
            if len(result_list) == 1:
                return result_list[0]
            else:
                return -1
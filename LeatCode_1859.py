class Solution(object):
    def sortSentence(self, s):
        list = s.split()
        result = [0] * len(list)
        a = 0
        for i in range(len(list)):
            a = int(list[i][-1])
            result[a-1] = list[i][:-1]
        
        return " ".join(result)
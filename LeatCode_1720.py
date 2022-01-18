class Solution(object):
    def decode(self, encoded, first):
        # first를 result에 넣고
        result = []
        result.append(first)
        
        # result[i]와 encoded[i]를 넣어 result[i+1] 생성
        for i in range(len(encoded)):
            result.append(result[i]^encoded[i])
        
        return result
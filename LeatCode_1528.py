class Solution(object):
    def restoreString(self, s, indices):
        # 새로운 리스트 만들기
        list = [0] * len(indices)
        
        # 새로운 리스트 인덱스에 indices의 값이 가리키는 곳에 s넣기
        for i in range(len(indices)):
            list[indices[i]] = s[i]
            
        # 리스트 붙이기
        return "".join(list)
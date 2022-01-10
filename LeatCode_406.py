class Solution:
    def reconstructQueue(self, people):
        people = people
        # -: 역순, 0이 앞에 있기에 0인덱스 먼저 내림차순, 이후 1인덱스 올림차순
        people.sort(key=lambda x: (-x[0], x[1]))
        list = []
        
        for i in people:
            list.insert(i[1], i)
        
        return list
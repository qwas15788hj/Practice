class Solution(object):
    def wordPattern(self, pattern, s):
        # 중복제거
        pattern_list = []
        for i in pattern:
            if i not in pattern_list:
                pattern_list.append(i)
        
        # 중복제거
        s_list = []
        for i in range(len(s.split())):
            if s.split()[i] not in s_list:
                s_list.append(s.split()[i])
        
        # 중복제거 같고, 갯수 같으면
        if len(pattern_list) == len(s_list):
            if len(pattern) == len(s.split()):
                for i in range(len(pattern_list)):
                    # 중복제거한 요소가 각각 몇번째 인덱스에 있는가! 인덱스 번호 찾기
                    list_1 = [v for v in range(len(pattern)) if pattern_list[i] == pattern[v]]
                    list_2 = [n for n in range(len(pattern)) if s_list[i] == s.split()[n]]
                    # 인덱스 번호가 다르면 다른 요소가 있는 것!
                    if list_1 != list_2:
                        return False
                return True
            else:
                return False
            
        else:
            return False
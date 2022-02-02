class Solution(object):
    def findAnagrams(self, s, p):
        result_list = []
        for i in range(len(s)-len(p)+1):
            a = s[i:i+len(p)]
            j = 0
            count = 0
            for j in range(len(p)):
                if a[j] in p and len(a) == len(set(a)):
                    count += 1
                    if count == len(p):
                        result_list.append(i)

        return result_list
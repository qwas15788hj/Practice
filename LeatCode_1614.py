class Solution(object):
    def maxDepth(self, s):
        count = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
                if result < count:
                    result = count
            elif s[i] == ")":
                count -= 1
                
        return result
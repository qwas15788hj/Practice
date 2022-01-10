class Solution(object):
    def mostWordsFound(self, sentences):
        s = sentences
        result = 0
        
        for i in range(len(s)):
            if result < len(s[i].split()):
                result = len(s[i].split())
                
        return result
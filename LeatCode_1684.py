class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed = set(allowed)
        count = len(words)
        for word in words:
            for i in range(len(word)):
                if word[i] not in allowed:
                    count -= 1
                    break
        
        return count
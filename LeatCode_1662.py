class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str_1 = ""
        str_2 = ""
        
        for i in range(len(word1)):
            str_1 += word1[i]
            
        for i in range(len(word2)):
            str_2 += word2[i]
        
        if str_1 == str_2:
            return True
        else:
            return False
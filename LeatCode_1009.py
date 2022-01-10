class Solution(object):
    def bitwiseComplement(self, n):
        n = n
        result = []
        a = bin(n)
        
        for i in range(2, len(a)):
            if a[i] == str(0):
                result.append(str(1))
            else:
                result.append(str(0))
                    
        return int("".join(result), 2)
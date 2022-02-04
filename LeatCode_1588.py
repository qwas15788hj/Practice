class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        x = []
        result = 0
        
        for i in range(1, len(arr)+1):
            if i%2 == 1:
                x.append(i)
                
        for i in x:
            j = 0
            while j+i < len(arr)+1:
                a = arr[j:j+i]
                j += 1
                result += sum(a)
        
        return result
class Solution(object):
    def xorOperation(self, n, start):
        arr = [0] * n
        for i in range(n):
            arr[i] = start + 2*i
        
        for i in range(1, n):
            arr[i] = arr[i-1] ^ arr[i]
        
        return arr[n-1]
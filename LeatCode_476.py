class Solution(object):
    def findComplement(self, num):
        self.num = num
        a = bin(self.num) # bin: 10진수 -> 2진수
        self.output = []
        
        for i in range(len(a)-2): # 2진수 앞에 '0b'빼고 진행
            # 2진수 1이면 0, 0이면 1로
            if(a[i+2]) == str(1):
                self.output.append(str(0))
            else:
                self.output.append(str(1))
        
        self.output = "".join(self.output) # 만들어진 2진수 리스트 붙이기
        
        return int(self.output, 2) # int: 2진수 -> 10진수
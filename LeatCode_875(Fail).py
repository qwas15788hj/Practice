class Solution(object):
    def minEatingSpeed(self, piles, h):
        count = h+1 # 몇번 나누어지는가
        n = 0.0 # 나누기 기준
        
        # count가 h와 같아질 때까지
        while count > h:
            count = 0
            n += 1
            # 하나씩 n으로 나눈후 최댓값 만큼 count
            for i in range(len(piles)):
                a = float(math.ceil(piles[i]/n))
                count += a

        return int(n)
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        # 공간이 2칸 이하 일때
        if len(flowerbed) < 3:
            if n > 1:
                return False
            
            # n이 1인데 1칸이라도 꽃이 있으면 false
            elif n == 1:
                for i in range(len(flowerbed)):
                    if flowerbed[i] == 1:
                        return False
                return True
            
            elif n == 0:
                return True
            
        # 공간이 3칸 이상 일때
        else:
            # 맨 앞과 그 뒤가 0이면 맨 앞에 심고 카운트
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                count += 1
            # 중간 꽃밭 현재 위치가 0이고 앞뒤가 0일때, 현재 위치에 심고 카운트
            for i in range(1, len(flowerbed)-1):
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
            # 맨뒤와 그 앞이 0일때, 맨뒤에 심고 카운트
            if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
                flowerbed[len(flowerbed)-1] = 1
                count += 1
            
            # 카운트(심을수있는곳)가 n보다 크거나 같으면 true 
            if count >= n:
                return True
            else:
                return False
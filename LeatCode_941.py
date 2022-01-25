class Solution(object):
    def validMountainArray(self, arr):   
        # 길이 3이하 Fasle
        if len(arr) < 3:
            return False
        else:
            # 가장 큰 수의 인덱스 값 찾기
            max_index = arr.index(max(arr))
            # 가장 큰 수가 맨 앞이나 맨 뒤에 있으면 False
            if max_index == 0 or max_index == len(arr)-1:
                return False
            
            else:
                # 등산 할때
                up_list = []
                up_list_sort = []
                for i in range(max_index+1):
                    up_list.append(arr[i])
                    up_list_sort.append(arr[i])
                up_list_sort.sort()
                # 1. 오를 때 같은 값이 있는지 => 있으면 False
                # 2. 계속 증가하지 않고 중간에 값이 끼어 있으면 False 
                if len(up_list) != len(set(up_list)) or up_list != up_list_sort:
                    return False
                
                # 하산 할때
                down_list = []
                down_list_sort = []
                for i in range(max_index, len(arr)):
                    down_list.append(arr[i])
                    down_list_sort.append(arr[i])
                down_list_sort.sort(reverse=True)
                # 1. 내려 갈 때 같은 값이 있는지 => 있으면 False
                # 2. 계속 감소하지 않고 중간에 값이 끼어 있으면 False
                if len(down_list) != len(set(down_list)) or down_list != down_list_sort:
                    return False
    
        return True
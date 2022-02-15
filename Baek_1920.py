import sys

def binarySearch(n_list, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    
    if n_list[mid] == target:
        return True
    elif n_list[mid] > target:
        return binarySearch(n_list, target, start, mid-1)
    else:
        return binarySearch(n_list, target, mid+1, end)

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for target in m_list:
    if binarySearch(n_list, target, 0, n-1) == True:
        print(1)
    else:
        print(0)
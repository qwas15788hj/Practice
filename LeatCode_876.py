import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        cur = head
        count = 0
        # cur 개수 구하기        
        while cur != None:
            cur = cur.next
            count += 1
            
        cnt = count//2 # 2+1 => 3
        
        slow = head
        for i in range (cnt):
            slow = slow.next   # slow = slow.next = None
            
        return slow
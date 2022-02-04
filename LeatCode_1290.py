# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        answer = ""
        while head.next != None:
            answer += str(head.val)
            head = head.next
        answer += str(head.val)
        
        return int(answer, 2)
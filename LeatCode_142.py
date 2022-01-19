# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        rabbit = head
        turtle = head
        result = head

        while rabbit!=None and rabbit.next!=None:
            rabbit = rabbit.next.next
            turtle = turtle.next
            # 순환인지 확인
            if(rabbit==turtle):
                while result!=None and turtle!=None:
                    if result == turtle:
                        return turtle
                    result = result.next
                    turtle = turtle.next
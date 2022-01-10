from collections import deque

class Solution(object):
    def connect(self, root):
        queue = deque([root])
        count = 1
        cnt = 1
        empty = None
        a = []
        
        while queue:
            node = queue.popleft()
            
            if count == 2**cnt - 1:
                node.next = None
                a.append(node)
                a.append(empty)
                cnt += 1
            else:
                node.next = queue[0]
                a.append(node)
                
            count += 1
            
        return root
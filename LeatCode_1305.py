# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        list = []
        if root1 != None:
            stack_1 = [root1]
            
            while stack_1:
                node = stack_1.pop()
                list.append(node.val)
                if node.left != None:
                    stack_1.append(node.left)
                if node.right != None:
                    stack_1.append(node.right)
                    
        else:
            pass
        
        if root2 != None:
            stack_2 = [root2]
            
            while stack_2:
                node = stack_2.pop()
                list.append(node.val)
                if node.left != None:
                    stack_2.append(node.left)
                if node.right != None:
                    stack_2.append(node.right)
                   
        else:
            pass
        
        list.sort()
        
        return list
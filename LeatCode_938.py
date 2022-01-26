# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root != None:
            stack = [root]
            result = low + high

            while stack:
                node = stack.pop()
                if node.val > low and node.val < high:
                    result += node.val
                if node.left != None:
                    stack.append(node.left)
                if node.right != None:
                    stack.append(node.right)
                    
        return result
class Solution(object):
    def sumRootToLeaf(self, root):
        list_1 = [] # 2진수
        list_2 = [] # 숫자
        count = 0
        cur = root
        
        while cur.left != None:
            list_1.append(cur.val)
            cur = cur.left
            
        list_1.append(cur.val)
        
        for i in range(len(list_1)):
            list_1[i] = str(list_1[i])
            
        a = "".join(list_1)
        list_2.append(int(a,2))

#         print(list_2)
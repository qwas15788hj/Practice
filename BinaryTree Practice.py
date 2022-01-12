# 노드 생성
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        
# 트리 생성
class BinaryTree():
    def __init__(self):
        self.root = None

    # 전위 순회 (Preorder)
    def preorder(self, n):
        if n != None:
            print(n.item, "", end="") # 노드 방문
            if n.left != None: # 왼쪽이 있을때
                self.preorder(n.left) # 왼쪽 서브 트리 순회
            if n.right != None: # 오른쪽이 있을때
                self.preorder(n.right) # 오른쪽 서브 트리 순회

    # 후위 순회 (Postorder)
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.item, "", end="")
            
    # 중위 순휘 (Inorder)
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(n.item, "", end="")
            if n.right:
                self.inorder(n.right)

    # 레벨 순회 (Levelorder)
    def levelorder(self, n):
        q = []
        q.append(n)
        while q:
            t = q.pop(0)
            print(t.item, "", end = "")
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

                
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

tree = BinaryTree()
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

tree.preorder(n1)
tree.postorder(n1)
tree.inorder(n1)
tree.levelorder(n1)
# 노드 정의: 노드 값, 노드가 가리키는 다음 곳
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self, data):
        self.head = Node(data) # 노드의 맨 앞인 헤드에 데이터 삽입
        
    # 맨뒤에 데이터 삽입
    def append(self, data):
        # cur을 헤드로 잡고 한 칸씩 뒤로 밈
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data) # next가 비었을 경우 data 삽입
        
    # 모든 리스트 뽑기
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    
    # 노드 인덱스 알아내기 (값X)
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node
    
    # 삽입
    def add_node(self, index, value):
        new_node = Node(value) # 넣을 새로운 노드 생성
        # 노드가 비었을 경우
        if index == 0:
            new_node.next = self.head # == None
            self.head = new_node
            return
        # 안비었을 경우
        # [1,2] -> [2,3] -> [3,4] ->[4,None] /=> [2,3] -> [5,None] -> [3,4] 
        node = self.get_node(index-1) # node = [2,3]
        a = node.next # a에 node.next의 값인 3을 저장
        node.next = new_node # node.next에 5인 new_node를 삽입
        new_node.next = a # new_node.next에 3인 a를 삽입

    # 삭제
    def delete_node(self, index):
        # 빈 노드일 경우
        if index == 0:
            self.head = self.head.next
            return
        # 안비었을경우
        # [1,2] -> [2,3] -> [3,4] -> [4,None] /=> [1,2] -> [2,4] -> [4,None]
        node = self.get_node(index-1) # node = [2,3]
        node.next = node.next.next # node.next(3)에 4인 node.next.next를 삽입

c = LinkedList(3) # 헤드 값 삽입
c.append(1)
c.append(2)
c.append(4)
# c.add_node(1,10)
# c.print_all()
# c.delete_node(2)
# c.print_all()
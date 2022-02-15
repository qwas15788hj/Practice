import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)] # n+1 개 빈 2차열 배열 초기화
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# 그래프마다 정렬
for i in range(n+1):
    graph[i].sort()

# DFS
def DFS(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

# BFS
def BFS(start):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

DFS(v)
print()
visited = [False]* (n+1)
BFS(v)
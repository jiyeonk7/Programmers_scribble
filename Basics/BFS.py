# Breadth-First Search, 너비 우선 탐색
from collections import deque

def bfs(graph, start, visited):     #start: 시작노드
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드의 인접노드를 담은 array
graph = [[],                       #0번 노드는 존재하지 X
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

visited = [False]*9

bfs(graph, 1, visited)
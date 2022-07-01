# Depth-First Search, 깊이 우선 탐색
def dfs(graph, v, visited):     # visited: 방문처리여부
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드의 인접노드를 담은 array
graph = [[],                    #0번 노드는 존재하지 X
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

visited=[False]*9               # 1-8번 노드라스 그냥 0을 사용하지 않는 방법으로 사용

dfs(graph,1,visited)
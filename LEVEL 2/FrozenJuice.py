#################################################문제#################################################
# connected component 찾기 문제
# N x M 크기의 얼음틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이때, 얼음틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
# 다음의 4x5 얼음틀 예시에서는 아이스크림이 총 3개 생성됩니다. 
# ex(00110      |00||0|
#    00011      |000|
#    11111
#    00000)     |00000|

# 조건 1: 첫 번쨰 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 <= N, M <= 1000)
# 조건 2: 두 번째 줄부터 N+1번째 줄까지 얼음틀의 형태가 주어집니다.
# 조건 3: 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.

# 출력: 한번에 만들 수 있는 아이스크림의 개수 출력

#################################################풀이#################################################
# 0 노드 있는 곳들이 연결이 되어 있다고 가정하고 그래프로 구성
# DFS 활용
# 1. 특정한 지점의 주변 상,하,좌,우를 살펴본 되에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 
#    있다면 해당 지점을 방문합니다.
# 2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면 연결된 모든 지점을 
#    방문할 수 있습니다.
# 3. 모든 노드에 대하여 1-2번의 과정을 반복 -> 방문하지 않은 지점의 수를 카운트합니다.

#################################################코드#################################################

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:          # 범위 벗어나는 경우에는 즉시 종료
        return False
    if graph[x][y] == 0:                                # 현재 노드를 아직 방문하지 않았다면 방문
        graph[x][y] = 1                                 # 해당 노드를 방문처리
        dfs(x-1 , y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = 4, 5
graph = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,0,0,0]]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
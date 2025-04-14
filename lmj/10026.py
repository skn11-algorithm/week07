import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline


N = int(input())
graph = []
visited = [[0] * (N) for _ in range(N)]
normal = 0
abnormal = 0


for i in range(N):
    graph.append(list(input().strip()))


def dfs(x, y, color):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited[x][y] = 1

    # 동서남북 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내에 있고 방문한 적이 없다면
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and visited[nx][ny] == 0:
            # 위 조건을 모두 만족하면서 탐색중인 색상과 같은 색상이면 탐색
            if graph[nx][ny] == color:
                dfs(nx, ny, color)

# normal 탐색
for color in ['R','G','B']: 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j,color)
                normal += 1

# abnormal 탐색 
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 방문 정보 초기화
visited = [[0] * (N) for _ in range(N)]

for color in ['R', 'B']: # 빨,파만 확인
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j,color)
                abnormal += 1

print(normal, abnormal)
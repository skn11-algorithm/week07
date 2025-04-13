import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == color:
                dfs(nx, ny, color)

count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            count1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[False]*n for _ in range(n)]

count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            count2 += 1

print(count1, count2)

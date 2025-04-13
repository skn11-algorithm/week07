import sys

input = sys.stdin.readline

n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
cnt1, cnt2 = 0, 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]
stack = []

def dfs(x, y):
    stack.append((x,y))
    visited[x][y] = True
    color = grid[x][y]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                stack.append((nx, ny))

# 적록색약 x
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            dfs(i,j)
            cnt1 += 1

# 적록색약 o
for i in range(n):
    for j in range(n):
        if grid[i][j]=='R':
            grid[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)
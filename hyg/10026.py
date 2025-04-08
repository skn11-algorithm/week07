# 적록색약

# 문제
# nxn 그리드에 r,g,b 중 하나를 칠한 그림
# 구역이 나눠져 있는데 구역은 같은 색으로 칠해져 있음
# 같은 색상이 상하좌우 인접해있으면 같은 구역
# 적록색약은 빨강==초록

# 입력
# n \n 그림 n개가 string으로

# 출력
# 적록색약이 아닌 사람이 봤을 때의 구역 개수 & 적록색약인 사람이 봤을 때의 구역 개수

# r,g,b 3가지를 중심으로 찾아야 하니까 dfs를 사용하자

import sys

input = sys.stdin.readline

n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
cnt1, cnt2 = 0, 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x, y):
    visited[x][y] = True
    color = grid[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color:
            dfs(nx, ny)

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
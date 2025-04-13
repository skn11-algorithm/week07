import sys
sys.setrecursionlimit(10000)
from collections import deque

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    field[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))

# 테스트 케이스 입력
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 위치 개수
    field = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())  # 배추 위치 (가로 y, 세로 x 주의!)
        field[x][y] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)

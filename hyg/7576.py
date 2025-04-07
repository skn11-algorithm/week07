# 토마토 골드5

# 문제
# 익은 토마토와 인접한 곳에 있으면 안 익은 토마토는 영향을 받아 익게 됨 -> 하루 걸림
# 대각선에는 영향 x

# 입력: 상자의 크기 m,n \n 토마토 정보 (1: 익은거, 0: 안익은거, -1: 없는거)
# 출력: 토마토가 모두 익을때까지의 최소 일수 - 만약 모든 토마토가 익었으면 0, 모두 안 익었으면 -1

# 풀이
# 익은 토마토 위치를 따로 queue에 저장해서 너비 우선으로 탐색

import sys
from collections import deque

input = sys.stdin.readline

m, n = list(map(int, input().split()))

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))

# 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))
            # day[nx][ny] = day[x][y] + 1

result = -1
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        result = max(result, j)
print(result-1)
# print(max(box[0])-1)
# print(day)
    


# 문제
# 가로, 세로, 대각선으로 연결되어 있으면 걸어갈 수 있음 -> 기존 bfs와 살짝 다름

# 입력
# 지도의 너비 w 높이 h \n 지도 (1: 땅, 0: 바다) \n 마지막 입력 0 0

# 출력
# 각 케이스에 대한 섬의 개수

import sys
from collections import deque

input = sys.stdin.readline
matrix = []
queue = deque()

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

if __name__ == '__main__':

    w, h = map(int, input().split())

    for i in range(h):
        matrix.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j]==1:
                queue.append((i,j))

    visited = [[False]*w for _ in range(h)]
    land = 0
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and matrix[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                
                flag = False
                for i in range(8):
                    nnx = nx + dx[i]
                    nny = ny + dy[i]

                    if 0 <= nnx < h and 0 <= nny <w and not visited[nnx][nny] and matrix[nnx][nny]==0:
                        flag = True
                
                if flag:
                    land += 1
    
    print(land)





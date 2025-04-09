# 문제
# 가로, 세로, 대각선으로 연결되어 있으면 걸어갈 수 있음 -> 기존 bfs와 살짝 다름

# 입력
# 지도의 너비 w 높이 h \n 지도 (1: 땅, 0: 바다) \n 마지막 입력 0 0

# 출력
# 각 케이스에 대한 섬의 개수

import sys
from collections import deque

input = sys.stdin.readline

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

def bfs(x, y):
    queue = deque([(x,y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and matrix[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny] = True 


if __name__ == '__main__':
    while True:
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            break

        matrix = []
        
        for i in range(h):
            matrix.append(list(map(int, input().split())))
        visited = [[False]*w for _ in range(h)]

        land = 0
    
        for i in range(h):
            for j in range(w):
                if matrix[i][j]==1 and not visited[i][j]:
                    bfs(i,j)
                    land += 1
        print(land)
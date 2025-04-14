# 0: 배추 x, 1: 배추 o
# 배추흰지렁이가 살고 있으면 인접한 다른 배추로 이동할 수 있음
# 총 몇 마리의 지렁이가 필요할까

import sys
from collections import deque

input = sys.stdin.readline



dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y, matrix, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and matrix[nx][ny]==1:
                visited[nx][ny] = True
                queue.append((nx,ny))
            


if __name__ == '__main__':
    t = int(input())
    
    while t>0:
        m, n, k = map(int, input().split())     # 가로, 세로, 위치의 개수
        
        matrix = [[0]*m for _ in range(n)]
        visited = [[False]*m for _ in range(n)]
        
        for _ in range(k):
            x, y = map(int, input().split())
            matrix[y][x] = 1
        
        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1 and not visited[i][j]:
                    bfs(i, j, matrix, visited)
                    count += 1
                    
        print(count)
        t -= 1
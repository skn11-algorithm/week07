# 문제
# 입력
# 출력

import sys
from collections import deque
input = sys.stdin.readline
matrix = []
result = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y, visited, count):
    land = 0
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny]=='1':
                land += 1
    
    result.append(land)

if __name__=='__main__':
    n = int(input())

    for i in range(n):
        matrix.append(list(map(str, input().split())))
    
    print(matrix)
    
    visited = [[False]*n for _ in range(n)]

    count = 0
    for i in range(0, n):
        for j in range(0, n):
            if not visited[i][j] and matrix[i][j]=='1':
                bfs(i, j, visited, count)
    
    print(len(result))
    for i in range(len(result)):
        print(result[count])
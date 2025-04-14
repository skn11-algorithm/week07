# 단지 번호 붙이기 
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N: # 이동할 좌표가 지도 범위에 있다면 
            if not visited[nx][ny] and graph[nx][ny] == 1:  # 방문x, 집이 있는 경우 
                dfs(nx, ny)

# 입력
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 단지 수 & 각 단지 집 수 저장
result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)


print(len(result))         
for num in sorted(result):  
    print(num)

from collections import deque
t = int(input()) # 몇 번의 테스트케이스인지

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y): # bfs 함수 구현
    q = deque()
    q.append([x, y])
    graph[x][y] = 0 # 방문 처리; 처리 방식: 표기된 1을 0으로 바꾸기
    
    while q: # q가 비었다 = 탐색 가능한 연속 영역 모두 탐색하였다.
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1: # 배추밭 범위를 벗어나지 않고 미방문한 좌표인 경우
                q.append([nx, ny])
                graph[nx][ny] = 0


for _ in range(t):  
    m, n, k = map(int, input().split())
    graph = [[0]*(n) for _ in range(m)] # 빈 배추밭
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1 # 배추 위치 표기
        
    cnt = 0
    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                bfs(graph, j, k)
                cnt+=1 # bfs 함수 들어갈때마다 count; 하나의 연속 영역이 끝날 때마다
    print(cnt)
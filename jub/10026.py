from collections import deque

def BFS(x,y):
    q.append((x,y)) # 시작위치 넣음
    dx = [-1,1,0,0] # 상하좌우 방향 설정
    dy = [0,0,-1,1]
    visited[x][y] = 1 # 시작위치는 방문했다고 표시
    while q: #큐가 빌 때까지 반복
        x, y = q.popleft() # 현재 좌표를 꺼냄
        for d in range(4): #상하좌우 반복문
            nx = x + dx[d]
            ny = y + dy[d]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                q.append((nx,ny))

# 입력받음
N = int(input())
a = [list(input()) for _ in range(N)] 
q = deque() # 큐선언 

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0 
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체크
            BFS(i,j) # bfs 가 한번 끝나면
            cnt1 += 1 # 하나의 색 영역을 다 돈 것이므로 증가

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G': # R과G를 구분 못하므로 G를 R로 바꿔서 같은 색으로 보이게함
            a[i][j] = 'R'

visited = [[0] * N for _ in range(N)] # 방문 기록 초기화
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt2 += 1

print(cnt1, cnt2) #결과 



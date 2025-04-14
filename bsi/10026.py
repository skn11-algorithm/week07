# import sys
# input = sys.stdin.readline

# countr = 0
# countg = 0
# countb = 0
# countrg=0


# def dfs(lst, x, y, visited):
#     visited[x][y] = True
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = x + dy[i]

#         if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and lst[nx][ny]=='R':
#             dfs(lst, nx, ny, visited)
#             countr += 1
#         if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and lst[nx][ny]=='G':
#             dfs(lst, nx, ny, visited)
#             countg += 1
#         if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and lst[nx][ny]=='B':
#             dfs(lst, nx, ny, visited)
#             countb += 1


# def dfs2(lst, x, y, visited):
#     visited[x][y] = True
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = x + dy[i]

#         if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and lst[nx][ny]=='R' or lst[nx][ny]=='G':
#             dfs(lst, nx, ny, visited)
#             countrg += 1
#         if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and lst[nx][ny]=='B':
#             dfs(lst, nx, ny, visited)
#             countb += 1




# n = int(input())
# lst = []
# visited = []
# for _ in range(n):
#     lst.append(list(map(input())))
#     visited.append(list(False*n))

# for i in lst:
#     for j in i:
#         dfs(lst, i, j, visited)

# for i in lst:
#     for j in i:
#         dfs2(lst, i, j, visited)

# print(countr+countb+countg, countrg + countb)

from collections import deque

def BFS(x,y):
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                q.append((nx,ny))


N = int(input())
a = [list(input()) for _ in range(N)]
q = deque()

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            BFS(i,j)
            cnt1 += 1

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt2 += 1

print(cnt1, cnt2)
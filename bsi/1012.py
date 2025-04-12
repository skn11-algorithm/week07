# import sys

# input = sys.stdin.readline

# t = int(input())    #  테스트 케이스
# def dfs(graph, v, visited):
#     if graph[v][0] not in M:
#         M.append(graph[v][0])
    
#     if graph[v][1] not in N and graph[v][0] not in M:
#         N.append(graph[v][1])
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i , visited)

# for _ in range(t):
#     lst = []   # 배추 위치 받을 곳
#     M=[]
#     N = []
#     m, n, k  = map(int, input().split())    # 가로, 세로, 배추 개수
#     print(m, n, k)
#     visited = [False] * k
#     for _ in range(k):
#         [x, y] = map(int, input().split())    #   배추 위치
#         lst.append([x, y])  # 2차원 리스트
#     for i in range(k):
#         dfs(lst, i, visited)
#     a = len(M) + len(N)
#     print(a)
#     visited = []
    

import sys
sys.setrecursionlimit(10000)  # 재귀 제한 초과 방지
input = sys.stdin.readline

def dfs(graph, x, y, visited):
    # 네 방향 정의 (상, 하, 좌, 우)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    visited[y][x] = True
    
    # 네 방향 모두 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 위치가 유효하고 배추가 있는지 확인
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1 and not visited[ny][nx]:
            dfs(graph, nx, ny, visited)

t = int(input().strip())  # 테스트 케이스 수

for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 개수
    
    # 필드 초기화 (0 = 배추 없음, 1 = 배추 있음)
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    # 배추 위치 표시
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    count = 0  # 필요한 지렁이 수
    
    # 필드의 각 위치 확인
    for y in range(n):
        for x in range(m):
            # 배추가 있고 방문하지 않았다면 DFS 시작
            if field[y][x] == 1 and not visited[y][x]:
                dfs(field, x, y, visited)
                count += 1  # 연결 요소 완료 후 지렁이 수 증가
    
    print(count)
# 유기농 배추
# 입력 : 테스트 케이스 개수 T / 배추밭가로길이 M 세로길이 N 배추 위치 개수 
# 출력 : 필요한 최수의 배추흰지렁이 마리 수 
# 아이디어 -> 배추밭 상태를 2차원으로 만들고 방문한 곳을 체크해가며 완전 탐색을 하자자

import sys
sys.setrecursionlimit(10**6)        #  DFS 깊이 들어가도 오류안나게하는 함수수
input = sys.stdin.readline

# dfs 정의
def dfs(x, y):
    # 현재 위치 방문처리
    visited[y][x] = True
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 있고 1이면(=배추이면), 아직 방문하지 않은 경우
        if (0 <= nx < M) and (0 <= ny < N) and graph[ny][nx] == 1 and not visited[ny][nx]:
            dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            # 배추 ㅇ 방문x 
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(j, i)
                count += 1
    
    print(count)
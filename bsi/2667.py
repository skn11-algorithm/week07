import sys
input = sys.stdin.readline

N = int(input())
graph = []  # 지도를 저장할 리스트
visited = [[False] * N for _ in range(N)]  # 방문 여부를 저장할 2차원 배열
complex_sizes = []  # 각 단지 내 집의 수를 저장할 리스트

# 지도 입력 받기
for _ in range(N):
    row = list(map(int, input().strip()))
    graph.append(row)

# DFS 함수 정의
def dfs(x, y):
    # 상, 하, 좌, 우 방향 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    visited[x][y] = True  # 현재 위치 방문 처리
    house_count = 1  # 현재 집을 포함해 1로 시작
    
    # 네 방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 유효한 범위이고, 집이 있으며, 아직 방문하지 않았다면
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
            # 연결된 집들의 수를 현재 집 수에 더함
            house_count += dfs(nx, ny)
    
    return house_count  # 총 집의 수 반환

# 모든 위치 확인
complex_count = 0  # 단지 수
for i in range(N):
    for j in range(N):
        # 집이 있고 아직 방문하지 않았다면
        if graph[i][j] == 1 and not visited[i][j]:
            # DFS 시작하고 단지 내 집의 수 저장
            complex_size = dfs(i, j)
            complex_sizes.append(complex_size)
            complex_count += 1  # 단지 수 증가

# 결과 출력
print(complex_count)  # 총 단지 수 출력
complex_sizes.sort()  # 단지 내 집의 수 오름차순 정렬
for size in complex_sizes:
    print(size)  # 각 단지 내 집의 수 출력
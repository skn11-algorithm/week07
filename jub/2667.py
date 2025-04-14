from collections import deque

# 상하좌우 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 #방문한 집은 0으로 바꿔 
    count = 1 #현재 단지 집개수 

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #지도 밖이면 무시 
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            #집(1) 이 있으면 계속 탐색색
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = [] # 단지 크기 저장 리스트
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: #집 있으면 bfs 시작 ㅇㅇ
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
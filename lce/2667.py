from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1  # 현재 단지의 집 수

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count

# 입력
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for num in result:
    print(num)

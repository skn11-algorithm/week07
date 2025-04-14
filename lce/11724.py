import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 입력
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선 입력 처리
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 개수 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)

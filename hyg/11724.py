import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

if __name__ == '__main__':
    n,m = map(int, input().split())
    graph = [[]*n for _ in range(n+1)]

    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    count = 0
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:  
            bfs(i, graph, visited)
            count += 1
    print(count)
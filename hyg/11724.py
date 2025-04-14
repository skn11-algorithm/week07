# 문제: 방향이 없는 그래프에서 연결 요소의 개수 구하기
# 입력: n,m \n 간선의 양 끝점 u,v
# 출력: 연결 요소의 개수

# 풀이 과정
# bfs 사용? 하면 될 거 같은데
# 이중 리스트로 저장 후 dfs -> 깊게 들어가면서 count 하나씩 증가
# 1 2 5
# 2 5
# 5 1 2
# 3 4
# 4 3 6

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

def dfs(v, graph, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

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
            # bfs(i, graph, visited)
            dfs(i, graph, visited)
            count += 1
    print(count)
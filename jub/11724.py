import sys
sys.setrecursionlimit(10**6) # 런타임에러 수정정
input = sys.stdin.readline

def dfs(graph, v, visit):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

n, m = map(int, input().split()) # 정점개수, 간선 개수 
graph = [[] for _ in range(n+1)]

for _ in range(m): # 그래프 만들기(인접리스트 방식)
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 무방향 -> 양쪽에 다 추가 

count = 0 
visit = [False] * (n+1)
for i in range(1, n+1):
    if not visit[i]:
        dfs(graph, i, visit)
        count += 1

print(count)

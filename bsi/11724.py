# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# # [0]의 값이 [1]에 있을시 이어져 있음 -> 찾은후 [0]의 값으로 다시 찾기

# def search(X, n):
#     target = X[n][0]
#     for i in range(len(X)):
#         if X[i][1] == target:
#             X.pop(i)
#             search(X, i)
#     count.append(True)
# X = []    
# for _ in range(M):
#     k = list(map(int, input().split()))
#     X.append(k)

# count = []
# search(X, 0)
# print(len(count))

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 노드의 수
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1

print(count)
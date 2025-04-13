import sys
from collections import deque

def bfs(n):
    queue=deque([n])
    visited[n]=True
    while queue:
        x=queue.pop()
        for num in graph[x]:
            if not visited[num]:
                queue.append(num)
                visited[num]=True
        
input=sys.stdin.readline
N,M = map(int,input().rstrip().split()) #정점, 간선 개수

graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)
count=0

for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        count+=1

print(count)


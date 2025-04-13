import sys
from collections import deque

def dfs(x,y,graph,visited):
    queue=deque([(x,y)])
    visited[x][y]=True

    while queue:
        x,y=queue.pop()   
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[x][y]==graph[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx,ny))

input=sys.stdin.readline
n=int(input())

graph=[list(input().strip()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

rg_graph=list(''.join(row).replace('R','G') for row in graph)
rg_visited=[[False]*n for _ in range(n)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

count=0
rg_count=0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j,graph,visited)
            count+=1

        if not rg_visited[i][j]:
            dfs(i,j,rg_graph,rg_visited)
            rg_count+=1

print(count)
print(rg_count)
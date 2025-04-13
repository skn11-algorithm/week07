import sys
from collections import deque

def dfs(x,y):
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


def rg_dfs(x,y):
    queue=deque([(x,y)])
    rg_visited[x][y]=True

    while queue:
        x,y=queue.pop()   
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[x][y]=='R' or graph[x][y]=='G':
                    if graph[nx][ny]=='G'or graph[nx][ny]=='R':
                        if not rg_visited[nx][ny]:
                            rg_visited[nx][ny]=True
                            queue.append((nx,ny))

                else:
                    if graph[x][y]==graph[nx][ny]:
                        if not rg_visited[nx][ny]:
                            rg_visited[nx][ny]=True
                            queue.append((nx,ny))

input=sys.stdin.readline
n=int(input())

graph=[list(input().strip()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
rg_visited=[[False]*n for _ in range(n)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]

count=0
rg_count=0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            count+=1

for i in range(n):
    for j in range(n):
        if not rg_visited[i][j]:
            rg_dfs(i,j)
            rg_count+=1


print(count)
print(rg_count)
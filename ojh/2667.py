import sys
from collections import deque

def bfs(a,b,count):
    queue=deque([(a,b)])
    graph[a][b]=0

    while queue:
        x,y=queue.pop()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                queue.append((nx,ny))
                count+=1
                graph[nx][ny]=0

    return count

input=sys.stdin.readline
n=int(input())

graph=[list(map(int,input().strip())) for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(i,j,1))

print(len(cnt))
print("\n".join(map(str,sorted(cnt))))
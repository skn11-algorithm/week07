import sys
from collections import deque

input=sys.stdin.readline
T=int(input().rstrip())
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y):
    queue=deque([(x,y)])
    cabbage[x][y]=0
    while queue:
        x,y=queue.pop()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and cabbage[nx][ny]==1:
                queue.append((nx,ny))
                cabbage[nx][ny]=0


for _ in range(T):
    M,N,K=map(int,input().rstrip().split()) # 열 , 행,
    cabbage=[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().rstrip().split()) #(x:열, y:행)
        cabbage[y][x]=1 
    
    count=0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j]==1:
                bfs(i,j)
                count+=1

    print(count)
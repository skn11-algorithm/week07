import sys
from collections import deque
input=sys.stdin.readline

def bfs(x,y):
    queue=deque([(x,y)])
    visited[x][y]=True

    while queue:
        x,y= queue.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<h and 0<=ny<w and ilands[nx][ny]==1:
                if not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny]=True


while True:
    w,h=map(int,input().rstrip().split())
    if w==0 and h==0:
        break

    ilands=[]
    visited=[[False]*w for _ in range(h)]

    count=0
    dx=[0,0,-1,1,-1,-1,1,1] # 행
    dy=[1,-1,0,0,-1,1,-1,1] # 열

    for i in range(h):
        ilands.append(list(map(int,input().rstrip().split())))

    for i in range(h): # 행
        for j in range(w): # 열
            if ilands[i][j]==1 and not visited[i][j]:
                bfs(i,j)
                count+=1

    print(count)
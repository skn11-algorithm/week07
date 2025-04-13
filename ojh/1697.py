# 최단거리 -> BFS
import sys
from collections import deque

def bfs(start): # 시작점
    queue=deque([start])
    visited[start]=0 # 시작점의 시간은 0

    while queue:
        x=queue.popleft()
        for i in (x+1,x-1,2*x):
            if 0<=i<=10**5 and visited[i]==-1:
                visited[i]=visited[x]+1 # 걸린시간을 위치에 저장
                queue.append(i)

N,K=map(int,sys.stdin.readline().rstrip().split()) # 수빈, 동생 위치
visited=[-1]*(10**5+1) # 0 ≤ N,K ≤ 100,000

bfs(N)
print(visited[K])
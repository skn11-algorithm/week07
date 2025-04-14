import sys
from collections import deque

def bfs(v):
    q = deque([v]) # 시작위치 
    while q:
        v = q.popleft() # 현재위치 꺼냄 
        if v == k: # 목표 위치 도달 시 
            return array[v] #해당 위치 까지 걸린시간 반환
        
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1 # 1초 추가 
                q.append(next_v) # 큐에 다음 위치 추가가


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))
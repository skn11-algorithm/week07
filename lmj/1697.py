# 숨바꼭질 ⭐⭐⭐
# 입력 : 수빈이 위치 점 N 동생위치 점 K 
# 출력 : 수빈이가 동생을 찾는 가장 빠른 시간 
# 최단거리 문제 : bfs?? 우선 10000 초과는 고려 안해도됨 

import sys
from collections import deque

N, K = map(int, input().split())
MAX = 100001 
visited = [0] * MAX

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        
        if now == K:
            return visited[now]
        
        for next in (now - 1, now + 1, now * 2): # 1초 후 이동과 순간이동 위치 
            if 0 <= next < MAX and visited[next] == 0:
                visited[next] = visited[now] + 1  # 현재까지 시간 +1
                queue.append(next)

print(bfs(N))

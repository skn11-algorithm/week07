import sys
import heapq

input = sys.stdin.readline

pq = []

def bfs(time, start, visited):
    heapq.heappush(pq, (time, start))
    
    while pq:
        time, n = heapq.heappop(pq)
        
        if visited[n]:
            continue
        visited[n] = True
        
        if n==k:
            print(time)
            break
        
        if n - 1 >= 0 and not visited[n - 1]:
            heapq.heappush(pq, (time + 1, n - 1))
        if n + 1 <= 100000 and not visited[n + 1]:
            heapq.heappush(pq, (time + 1, n + 1))
        if 2 * n <= 100000 and not visited[2 * n]:
            heapq.heappush(pq, (time + 1, 2 * n))
    

if __name__ == '__main__':
    n,k = map(int, input().split())
    visited = [False]*100001
    
    bfs(0, n, visited)
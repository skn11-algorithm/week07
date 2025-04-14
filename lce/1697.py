from collections import deque

def bfs(start, target):
    visited = [0] * 100001
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        if current == target:
            return visited[current]
        
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == 0:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# 입력
n, k = map(int, input().split())
print(bfs(n, k))

from collections import deque

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 


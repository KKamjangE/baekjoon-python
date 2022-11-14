from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    que = deque([(x-1, y-1)])
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            my = y + dy[i]
            
            if 0 <= nx < N and 0 <= my < M and matrix[nx][my] == 1:
                que.append((nx, my))
                matrix[nx][my] += matrix[x][y]
                
    return matrix[N-1][M-1]

N, M = map(int, input().split())

matrix = [list(map(int, input().strip()))for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

print(bfs(1, 1))
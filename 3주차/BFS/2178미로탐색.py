from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y): # BFS
    que = deque([(x-1, y-1)])
    while que:
        x, y = que.popleft() # 현재 위치 저장
        
        for i in range(4): # 주어진 좌표에서 상하좌우 좌표로 이동할 수 있는지 체크
            nx = x + dx[i] # x 좌표 이동 방향
            ny = y + dy[i] # y 좌표 이동 방향

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1: # 0 ~ N, M 사이에 있고 해당 칸이 1일 경우
                que.append((nx, ny)) # 좌표 push
                matrix[nx][ny] += matrix[x][y] # 방문 처리
                
    return matrix[N-1][M-1]
    
N, M = map(int, input().split()) # 미로 y, x 좌표

matrix = [] # 인접 그래프 생성

for _ in range(N):
    matrix.append(list(map(int, input().strip()))) # 인접 그래프에 입력

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 좌, 우, 위, 아래 방향 이동

print(bfs(1, 1))
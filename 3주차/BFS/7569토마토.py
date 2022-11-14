import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

dx = [-1, 1, 0, 0, 0, 0] # x 좌표
dy = [0, 0, -1, 1, 0, 0] # y 좌표
dz = [0, 0, 0, 0, -1 ,1] # z 좌표

g = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # 토마토 상자

que = deque() # 덱 생성 

def bfs():
    while que:
        z, x, y = que.popleft() # 토마토 위치 저장
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1 < nx < N and -1 < ny < M and -1 < nz < H: # N, M, H 안에 들어 있다면
                if g[nz][nx][ny] == 0: # 토마토가 없다면
                    g[nz][nx][ny] = g[z][x][y]+1 # 하루 + 해서 방문 처리
                    que.append((nz,nx,ny)) # 익은 토마토 push

for i in range(H):
    for j in range(N):
        for k in range(M):
            if g[i][j][k] == 1:
                que.append((i, j, k)) # 익은 토마토가 있는 위치 push

bfs()
flag = 0
result = -2

for i in range(H):
    for j in range(N):
        for k in range(M):
            if g[i][j][k] == 0: # 안 익은 토마토가 있다면
                flag = 1
            result = max(result, g[i][j][k]) # 익은 토마토 일수와 비교해서 갱신

if flag == 1:
    print(-1) # 다 익을 수 없음
elif result == -1:
    print(0) # 이미 다 익은 토마토라면
else:
    print(result-1) # 토마토가 다 익은 일수
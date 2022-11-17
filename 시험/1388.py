# 바닥 장식
# 솔루션 참고
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global ans
    que = deque([(x, y)])
    
    while que:
        a, b = que.popleft()
        if g[a][b] == '-': # 나무 판자가 '-'
            g[a][b] = 0 # 방문 처리
            if b+1 < M and g[a][b+1] == '-': # y좌표가 최대를 넘지않고 '-'
                que.append((a, b+1)) # 큐 push
        
        if g[a][b] == '|': # 나무 판자가 '|'
            g[a][b] = 0 # 방문 처리
            if a+1 < N and g[a+1][b] == '|': # x좌표가 최대를 넘지않고 '|'
                que.append((a+1, b)) # 큐 push
    
N, M = map(int, input().split()) # 집의 크기

g = [list(input().strip()) for _ in range(N)] # 집 지도

ans = 0

for i in range(N):
    for j in range(M):
        if g[i][j] != 0: # 방문처리가 되지 않았을 경우에만
            bfs(i, j) # bfs
            ans += 1 # 나무 판자 + 1

print(ans)
# 내리막 길
# 솔루션 참고
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, y):
    if x == M-1 and y == N-1: # 목적지 도착시 리턴 1
        return 1

    if visit[x][y] == -1: # 방문 체크
        visit[x][y] = 0 # 방문 처리
        
        for i in range(4): # 방향
            nx = x + dx[i]
            my = y + dy[i]
            
            if 0 <= nx < M and 0 <= my < N: # 지도 범위 체크
                if map_arr[x][y] > map_arr[nx][my]: # 내리막길 체크
                    visit[x][y] += dfs(nx, my) # 사용한 길 + 1
                
    return visit[x][y]

M, N = map(int, input().split())

map_arr = [list(map(int, input().split())) for _ in range(M)]

visit = [[-1] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(dfs(0, 0))

# print(*map_arr, *visit, sep='\n')
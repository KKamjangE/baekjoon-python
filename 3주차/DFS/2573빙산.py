import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] == False and g[nx][ny] > 0:
                visit[nx][ny] = True
                dfs(nx,ny)


N, M = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

g = [list(map(int, input().split())) for _ in range(N) ]

ans = 0
ice_num = 0
flag = False

while True:
    visit = [[False] * (M) for _ in range(N)]
    ice_num = 0
    
    for i in range(N):
        for j in range(M):
            if visit[i][j] == False and g[i][j] > 0:
                ice_num +=1
                if ice_num > 1:
                    flag = True
                    break
                visit[i][j] = True
                dfs(i, j)
        if flag: break

    if ice_num == 0:
        ans = 0
        break
    elif ice_num > 1:
        break

    for i in range(N):
        for j in range(M):
            if g[i][j] > 0:
                water = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if g[nx][ny] == 0 and not visit[nx][ny]:
                            water += 1
                
                g[i][j] -= water
                if g[i][j] < 0:
                    g[i][j] = 0
                
    ans += 1
    
print(ans)
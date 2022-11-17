import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y): # 빙산이 1개 이상인지 검사
    for k in range(4): # 방향
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M: # 범위 안에 있다면
            if visit[nx][ny] == False and g[nx][ny] > 0: # 방문하지 않았고 빙산이라면
                visit[nx][ny] = True # 방문처리
                dfs(nx,ny) # 다음빙산으로


N, M = map(int, input().split()) # 지도 x, y

dx = [1, -1, 0, 0] # x 좌표
dy = [0, 0, 1, -1] # y 좌표

g = [list(map(int, input().split())) for _ in range(N) ] # 빙산 지도

ans = 0 # 몇년이 걸리는지?
ice_num = 0 # 빙산의 개수
flag = False # 체크

while True:
    visit = [[False] * (M) for _ in range(N)] # 방문 리스트 초기화
    ice_num = 0 # 빙산의 개수 초기화
    
    for i in range(N): # x 좌표 그래프
        for j in range(M): # y 좌표 그래프
            if visit[i][j] == False and g[i][j] > 0: # 방문하지 않은 빙산이라면
                ice_num +=1 # 빙산 +1개
                if ice_num > 1: # 빙산이 1개보다 많으면
                    flag = True # 체크 처리
                    break # 정지
                visit[i][j] = True # 방문 처리
                dfs(i, j) # 빙산 몇개인지 검사 시작
        if flag: break # 정지

    if ice_num == 0: # 빙산이 분해되지 않고 다 녹으면
        ans = 0 # 0 출력
        break
    elif ice_num > 1: # 빙산이 1개보다 많으면
        break # 정지

    for i in range(N): # x 좌표 그래프
        for j in range(M): # y 좌표 그래프
            if g[i][j] > 0: # 빙산이라면
                water = 0 # 주변 바다 개수 초기화
                for k in range(4): # 방향
                    nx = i + dx[k] # x 좌표
                    ny = j + dy[k] # y 좌표
                    if 0 <= nx < N and 0 <= ny < M: # 범위 안에 있다면
                        if g[nx][ny] == 0 and not visit[nx][ny]: # 방문하지 않은 바다면
                            water += 1 # 바다 개수 + 1
                
                g[i][j] -= water # 바다 개수의 영향만큼 -n
                if g[i][j] < 0: # 빙산이 음수 값이 나오면
                    g[i][j] = 0 # 0으로 변경
                
    ans += 1 # + 1년
    
print(ans)
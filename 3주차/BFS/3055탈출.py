import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split()) # 지도 크기

visit = [[False] * C for _ in range(R)] # 방문 리스트
g = [list(input().strip()) for _ in range(R)] # 지도
count = 0 # 시간

sonic = deque() # 고슴도치 위치
water = deque() # 물 위치

dx = [1, -1, 0, 0] # x 좌표
dy = [0, 0, 1, -1] # y 좌표

for i in range(R):
    for j in range(C):
        if g[i][j] == '*': # 물 좌표 저장
            water.append((i, j))
            visit[i][j] = True # 방문 처리
        elif g[i][j] == 'S': # 고슴도치 좌표 저장
            sonic.append((i, j)) # 방문 처리
            visit[i][j] = True
        elif g[i][j] == "X": # 돌 좌표
            visit[i][j] = True # 방문 처리
            
while sonic: # 고슴도치가 이동 가능할 때만
    for i in range(len(water)): # 물 확장
        wx, wy = water.popleft() # 물의 x, y 좌표
        for j in range(4): # 이동 가능 방향 체크
            nx = wx + dx[j] # x 좌표
            ny = wy + dy[j] # y 좌표
            if 0 <= nx < R and 0 <= ny < C: # 물이 지도 밖으로 나가지 않으면
                if g[nx][ny] == '.': # 빈 공간일 때만
                    water.append((nx, ny)) # 이동 한 물 좌표 저장
                    g[nx][ny] = '*' # 물 처리
                    visit[nx][ny] = True # 방문 처리
                    
    count += 1 # 시간 +

    for _ in range(len(sonic)): # 고슴도치 이동
        sx, sy = sonic.popleft() # 고슴도치 x, y 좌표
        for i in range(4): # 이동 가능 방향 체크
            nx = sx + dx[i] # x 좌표
            ny = sy + dy[i] # y 좌표
            if 0 <= nx < R and 0 <= ny < C: # 지도 밖으로 나가지 않는 경우
                if g[nx][ny] == '.' and not visit[nx][ny]: # 빈 공간이고 아직 방문하지 않은 경우
                    sonic.append((nx, ny)) # 이동한 위치 저장
                    visit[nx][ny] = True # 방문처리
                elif g[nx][ny] == 'D': # 이동하는 구역이 D 라면
                    print(count) # 시간 출력
                    exit() # 탈출
                    
print('KAKTUS') # 탈출 실패
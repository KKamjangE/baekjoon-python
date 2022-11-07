import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

maps = [[0] * (n+1) for _ in range(n+1)] # 보드 생성

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    maps[x][y] = 2 # 사과 자리 표시 (2)
    
rotation = {}
l = int(sys.stdin.readline())

for _ in range(l):
    sec, rotate = sys.stdin.readline().split()
    rotation[int(sec)] = rotate # 시간에 따라 회전 정보 딕셔너리로 저장
    
time = 0
dx = [1,0,-1,0] # 뱀의 x 4방향 움직임
dy = [0,1,0,-1] # 뱀의 y 4방향 움직임
x, y = 1, 1 # 뱀의 좌표
maps[y][x] = 1 # 뱀 위치 지도에 표시 (1)
d = 0 # 뱀의 방향
snake = deque([(1, 1)]) # 뱀의 길이

while True:
    nx, ny = x+dx[d], y+dy[d] # 뱀의 움직임 저장
    if nx <= 0 or ny <= 0 or nx>n or ny>n or (nx, ny) in snake: # 종료 조건
        break
    
    if maps[ny][nx] != 2: # 사과가 없다면 꼬리 줄이기
        a, b = snake.popleft() # 뱀 줄어듬
        maps[b][a] = 0 # 꼬리가 있던 위치 삭제(0)
    
    x, y = nx, ny # 뱀의 위치 갱신
    maps[y][x] = 1 # 뱀 이동
    snake.append((nx, ny)) # 뱀 늘어남
    time += 1
    
    if time in rotation.keys(): # 현재 시간에 해당하는 방향 전환이 있을 경우
        if rotation[time] == "D": # 오른쪽
            d = (d+1)%4
        else: # 왼쪽
            nd = 3 if d == 0 else d - 1
            d = nd
print(time+1)
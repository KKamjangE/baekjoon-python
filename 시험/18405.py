# 경쟁적 전염
from collections import deque
import heapq
import sys
input = sys.stdin.readline

def bfs(x, y):
    global my_time
    while priority_que: # 현재 퍼지는 바이러스가 다 처리될 때까지
        if my_time == S: # 만약 정해진 시간대가 된다면
            break # 정지
        
        virus_num, row, col = heapq.heappop(priority_que) # 바이러스 종류, x, y 좌표 빼오기

        for direc_idx in range(4): # 4방향 체크
            eidt_row = row + d_row[direc_idx]
            edit_col = col + d_col[direc_idx]
            if 0 <= eidt_row < N and 0 <= edit_col < N: # 시험관 범위 안에 있다면
                if g[eidt_row][edit_col] == 0: # 바이러스가 아직 퍼지지 않은 공간이라면
                    g[eidt_row][edit_col] = virus_num # 바이러스 처리
                    waiting_que.append((virus_num, eidt_row, edit_col)) # 다음 퍼지는 바이러스에 방금 처리한 공간 저장

        if not priority_que: # 현재 퍼지는 바이러스가 다 처리됐다면
            my_time += 1 # 시간 + 1
            while waiting_que: # 다음 퍼지는 바이러스들을 현재 리스트에 저장
                heapq.heappush(priority_que, waiting_que.popleft())

    return g[x - 1][y - 1] # 정해진 좌표에 바이러스 종류 반환

N, K = map(int, input().split()) # 시험관 크기 N^N, 바이러스 개수 K

g = [list(map(int, input().split())) for _ in range(N)]  # 시험관안의 바이러스 배치 2차원 배열

priority_que = [] # 현재 퍼지는 바이러스

S, X, Y = map(int, input().split())  # 시간 초, x, y 좌표

d_row = [1, -1, 0, 0] # x 좌표
d_col = [0, 0, 1, -1] # y 좌표

my_time = 0 # 초

waiting_que = deque() # 다음에 퍼지는 바이러스

for row in range(N):
    for col in range(N):
        if g[row][col] != 0: # 바이러스 라면
            data = (g[row][col], row, col) # 바이러스 종류, x, y 좌표
            heapq.heappush(priority_que, data) # heapq로 push
            
print(bfs(X, Y))
# 경쟁적 전염
from collections import deque
import heapq
import sys
input = sys.stdin.readline
def bfs(x, y):
    global my_time
    while priority_que:
        if my_time == S:
            break
        virus_num, row, col = heapq.heappop(priority_que)
        for direc_idx in range(4):
            eidt_row = row + d_row[direc_idx]
            edit_col = col + d_col[direc_idx]
            if 0 <= eidt_row < N and 0 <= edit_col < N:
                if g[eidt_row][edit_col] == 0:
                    g[eidt_row][edit_col] = virus_num
                    waiting_que.append((virus_num, eidt_row, edit_col))
        if not priority_que:
            my_time += 1
            while waiting_que:
                heapq.heappush(priority_que, waiting_que.popleft())
    return g[x - 1][y - 1]
N, K = map(int, input().split())  # 지도의 크기
g = [list(map(int, input().split())) for _ in range(N)]  # 지도
priority_que = []
S, X, Y = map(int, input().split())  # 시간 초, x, y 좌표
d_row = [1, -1, 0, 0]
d_col = [0, 0, 1, -1]
my_time = 0
waiting_que = deque()
for row in range(N):
    for col in range(N):
        if g[row][col] != 0:
            data = (g[row][col], row, col)
            heapq.heappush(priority_que, data)
print(bfs(X, Y))
import sys
import heapq
input = sys.stdin.readline

def dijkstra():
    dx = [1, -1, 0, 0] # x 좌표 정보
    dy = [0, 0, 1, -1] # y 좌표 정보
    que = [] # 큐
    heapq.heappush(que, [0, 0, 0]) # 시작점
    visit[0][0] = 1 # 시작점 방문 처리
    while que:
        a, x, y = heapq.heappop(que) # a = 제거한 벽, x, y = 좌표
        if x == N - 1 and y == N - 1: # 끝점에 도달했을 경우
            print(a) # 제거한 벽 수 출력
            return
        for i in range(4):
            nx = x + dx[i] # x 좌표
            ny = y + dy[i] # y 좌표
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0: # 해당 좌표로 갈 수 있는지 검사, 방문 체크
                visit[nx][ny] = 1 # 방문 처리
                if g[nx][ny] == 0: # 최단 거리에서 벽이 막힌 경우
                    heapq.heappush(que, [a + 1, nx, ny]) # 벽을 제거 + 1, x, y 좌표 저장
                else:
                    heapq.heappush(que, [a, nx, ny])

N = int(input()) # 미로의 길이

g = [list(map(int, input().strip())) for _ in range(N)] # 미로 그래프

visit = [[0] * N for _ in range(N)] # 방문 리스트

dijkstra()
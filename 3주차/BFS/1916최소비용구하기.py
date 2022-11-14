import sys
import heapq
input = sys.stdin.readline
    
def dijkstra(v):
    visit[v] = 0 # 첫번째 정점 비용 0
    que = [(v, 0)] # 비용과 현재 정점 위치 저장
    
    while que:
        current, x = heapq.heappop(que) # 현재위치, 비용
        if visit[current] < x: # 현재 위치까지 오는 비용이 새로운 비용보다 작다면 생략
            continue
        
        for dest, w in g[current]: # 현재 정점에서의 간선과, 비용
            cost = visit[current] + w # 현재 정점까지 오는데 누적된 비용과 다음 간선 비용 더해서 저장
            if visit[dest] > cost: # 목적지 비용보다 작다면
                visit[dest] = cost # 비용 교체
                heapq.heappush(que, (dest, cost)) # 큐에 목적지와 비용 저장
    
N = int(input()) # 도시 개수
M = int(input()) # 버스 개수

g = [[]for _ in range(N + 1)]
for i in range(M):
    a, b, x = map(int, input().split()) # 간선 a to b, 비용
    g[a].append((b, x))

start, end = map(int, input().split()) # 시작점, 끝점

visit = [1e9 for _ in range(N + 1)] # 비용 리스트

dijkstra(start)
print(visit[end])
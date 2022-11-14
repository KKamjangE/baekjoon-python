from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, K, X = map(int, input().split())# 도시개수, 도로개수, 특정거리, 출발도시 번호
g = [[]for _ in range(N+1)] # 인접 그래프
distance = [0] * (N + 1) # 거리 정보
visit = [False] * (N + 1) # 방문 리스트

for _ in range(M): # 인접 그래프에 간선 입력
    a, b = map(int, input().split())
    g[a].append(b) # 단방향이라 하나만 입력

def bfs(v): # BFS
    ans = []
    que = deque([v])
    visit[v] = True
    distance[v] = 0 # 정점 자신의 거리는 0
    while que:
        node = que.popleft() # 현재 정점 저장
        for i in g[node]: # 현재 정점의 간선만큼
            if not visit[i]:
                visit[i] = True
                que.append(i)
                distance[i] = distance[node] + 1 # 다음 정점 거리 정보에 현재 정점 +1(거리) 저장
                if distance[i] == K: # 특정 거리와 같다면
                    ans.append(i)
    if len(ans) == 0: # 특정 거리 안에 없다면 -1 출력
        print(-1)
    else:
        ans.sort() # 오름차순으로
        print(*ans, sep='\n')

bfs(X)
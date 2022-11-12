import sys
from collections import deque
sys.setrecursionlimit(5000)

def bfs(v):
    que = deque([v])
    visit[v] = True
    
    while que:
        node = que.popleft()
        for i in graph[node]:
            if not visit[i]:
                visit[i] = True
                que.append(i)

N, M = map(int, sys.stdin.readline().split()) # 정점개수, 간선개수

graph = [[]for _ in range(N+1)] # 인접 리스트 생성

for _ in range(M): # 인접 리스트에 간선 추가
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
visit = [False] * (N+1)
    
cnt = 0
    
for i in range(1, N+1):
    if visit[i] == False:
        if not graph[i]:
            cnt += 1
            visit[i] = True
        else:
            bfs(i)
            cnt += 1
            
print(cnt)
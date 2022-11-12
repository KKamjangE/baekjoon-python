import sys
sys.setrecursionlimit(5000)

def dfs(v): # DFS
    
    visit[v] = True # 방문 처리

    for i in graph[v]:
        if not visit[i]:
            dfs(i)

N, M = map(int, sys.stdin.readline().split()) # 정점개수, 간선개수

graph = [[]for _ in range(N+1)] # 인접 리스트 생성

for _ in range(M): # 인접 리스트에 간선 추가
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
visit = [False] * (N + 1)
    
cnt = 0
    
for i in range(1, N+1): # 다수의 그래프가 끊어져 있기 때문에 모든 노드를 검사
    if visit[i] == False: # 방문 체크
        if not graph[i]: # 해당 정점이 연결된 그래프가 없다면
            cnt += 1
            visit[i] = True # 방문 처리
        else: # 연결된 그래프가 있다면
            dfs(i)
            cnt += 1
            
print(cnt)
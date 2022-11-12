from collections import deque

def dfs(graph, v, visited): # 깊이 우선 탐색
    visited[v] = True # 방문 체크
    print(v, end=' ') # 출력

    for i in graph[v]: # 인접리스트안의 간선마다
        if not visited[i]: # 방문을 안했다면
            dfs(graph, i, visited)


def bfs(graph,v,visited): # 넓이 우선 탐색
    queue=deque([v])

    visited[v]=True

    while queue:
        v=queue.popleft() # 큐 값 제거하고 출력
        print(v, end=' ')

        for i in graph[v]: # 인접리스트안의 간선마다
            if not visited[i]: # 방문을 안했다면
                queue.append(i) # 큐에 추가
                visited[i]=True # 방문 체크


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] # 인접리스트 생성

for _ in range(M): # 인접리스트에 간선 추가
    a, b = map(int, input().split())
    # 무방향 대칭이기 때문에 양쪽에 다 넣어줌
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N + 1) # 방문 리스트
dfs(graph,V,visited)
visited = [False] * (N + 1) # 방문 리스트
print()
bfs(graph,V,visited)
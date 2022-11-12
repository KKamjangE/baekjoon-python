import sys
sys.setrecursionlimit(5000)

# dfs로 그래프를 탐색한다.
def dfs(start, depth):

    #해당 노드 방문체크 한다.
    visited[start] = True

    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를탐색한다.
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)] # 인접 리스트 생성

for _ in range(M): # 인접 리스트에 간선 추가
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)

count = 0  # 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs탐색을 돈다.
            count += 1  # 개수를 +1

print(count)
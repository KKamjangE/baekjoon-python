import sys
sys.setrecursionlimit(5000)

def dfs(v): # DFS
    global count
    visit[v] = True # 방문 처리
    
    for i in g[v]: # 해당 노드에 연결된 간선들
        if not visit[i]: # 방문 체크
            count += 1 # 카운팅
            dfs(i) # 재귀 호출

n = int(sys.stdin.readline()) # 정점의 개수
m = int(sys.stdin.readline()) # 간선의 개수

count = 0 # 카운터
g = [[] for _ in range(n + 1)] # 빈 인접 리스트 생성

for _ in range(m): # 인접 리스트에 간선 저장
    x, y = map(int, sys.stdin.readline().split())
    # 무방향이기 때문에 양쪽에 입력해준다
    g[x].append(y)
    g[y].append(x)

visit = [False] * (n + 1) # 방문 리스트 생성

dfs(1) # 루트가 1로 주어진다
print(count)
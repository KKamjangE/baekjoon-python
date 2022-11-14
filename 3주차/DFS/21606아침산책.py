import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v):
    global count
    visit[v] = True

    for i in g[v]:
        if visit[i] == False:
            visit[i] = True
            if place[i-1] == place[v-1]:
                return
            if place[i-1] == 1:
                count += 1
            dfs(i)

N = int(input()) # 정점의 개수

place = list(map(int, input().strip())) # 장소 정보 1 = 실내 0 = 실외

g = [[] for _ in range(N + 1)] # 인접 리스트

for _ in range(N-1): # 인접 리스트에 간선 입력
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
    
count = 0

for i in range(1, N+1):
    if place[i-1] == 1:
        visit = [False] * (N+1)
        dfs(i)
    
print(count)
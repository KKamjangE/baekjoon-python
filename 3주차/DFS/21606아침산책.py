import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    global ans
    global temp
    if place[v-1] == 1: # 본인이 실내
        for i in g[v]:
            if place[i-1] == 1: # 인접한 곳이 실내라면
                ans += 1 # 실내와 인접한 실내 카운팅
    elif place[v-1] == 0 and visit[v] == False: # 본인이 실외
        visit[v] = True # 방문처리
        
        for i in g[v]:
            if place[i-1] == 1: # 인접한 곳이 실내라면
                temp+=1 # 실외와 인접한 실내 카운팅
            elif place[i-1] == 0 and visit[i] == False: # 인접한 곳이 실외라면
                dfs(i)

N = int(input()) # 정점의 개수

place = list(map(int, input().strip())) # 장소 정보 1 = 실내, 0 = 실외

g = [[] for _ in range(N + 1)] # 인접 리스트

for _ in range(N-1): # 인접 리스트에 간선 입력
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
    
ans = 0

visit = [False for _ in range(N + 1)] # 방문 리스트

for i in range(1, N+1): # 각각의 정점마다
    temp = 0
    dfs(i)
    ans += temp*(temp-1) # 실외와 인접한 실내 수 * (실외와 인접한 실내 수 - 1)

print(ans)
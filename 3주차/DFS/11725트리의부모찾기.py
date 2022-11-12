import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 제한 조정

n = int(sys.stdin.readline())

g = [[] for _ in range(n+1) ] # 인접 리스트 생성

for _ in range(n-1): # 인접 리스트 간선 입력 주어지는 개수가 n-1개
    x, y = map(int, sys.stdin.readline().split())
    g[x].append(y)
    g[y].append(x)

parent = [0 for _ in range(n+1)] # 부모 리스트

def dfs(v): # DFS
    
    for i in g[v]: # 인접리스트[v]의 간선 수 만큼
        if parent[i] == 0: # 부모 체크
            parent[i] = v # 부모 설정
            dfs(i) # 재귀 호출
            
dfs(1) # 루트는 1로 주어짐

print(*parent[2:], sep='\n') # 0번은 빈칸 1번은 루트이기 때문에 2부터 출력
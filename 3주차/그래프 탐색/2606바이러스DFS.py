import sys
sys.setrecursionlimit(5000)

def dfs(v):
    global count
    visit[v] = True
    
    for i in g[v]:
        if not visit[i]:
            count += 1
            dfs(i)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

count = 0
g = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    g[x].append(y)
    g[y].append(x)

visit = [False] * (n + 1)

dfs(1)  
print(count)
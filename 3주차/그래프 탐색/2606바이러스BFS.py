import sys
from collections import deque
sys.setrecursionlimit(5000)

def bfs(v):
    global count
    que = deque([v])
    visit[v] = True
    while que:
        node = que.popleft()
        for i in g[node]:
            if not visit[i]:
                que.append(i)
                visit[i] = True
                count += 1

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

count = 0
g = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    g[x].append(y)
    g[y].append(x)

visit = [False] * (n + 1)

bfs(1)
print(count)
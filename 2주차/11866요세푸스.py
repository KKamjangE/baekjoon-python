from collections import deque

n, k = map(int, input().split())

que = deque(i for i in range(1, n+1))
ans = []

while que:
    for i in range(k-1):
        que.append(que.popleft())
    ans.append(que.popleft())
    
print('<', end='')
print(*ans, sep=', ', end='')
print('>')
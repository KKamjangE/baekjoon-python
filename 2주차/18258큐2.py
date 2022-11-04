import sys
from collections import deque

n = int(input())

que = deque()

def q(a):
    if a[0] == 'push':
        que.append(a[1])
    elif a[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.popleft()
    elif a[0] == 'size':
        print(len(que))
    elif a[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif a[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

for i in range(n):
    a = list(sys.stdin.readline().split())
    q(a)
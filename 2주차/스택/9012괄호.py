import sys

n = int(input())

for _ in range(n):
    stack = []
    VPS = True
    arr = sys.stdin.readline()
    for a in arr:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if not stack:
                VPS = False
                break
            elif stack:
                stack.pop()

    if not stack and VPS == True:
        print('YES')
    else:
        print('NO')
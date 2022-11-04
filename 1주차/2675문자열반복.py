import sys
t = int(input())
for i in range(t):
    a, b = sys.stdin.readline().split()
    x = [b[i]*int(a) for i in range(len(b))]
    print(''.join(x))
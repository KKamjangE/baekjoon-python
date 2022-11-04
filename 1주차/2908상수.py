import sys
a, b = sys.stdin.readline().split()
if a[::-1] > b[::-1]:
    print(a[::-1])
else:
    print(b[::-1])
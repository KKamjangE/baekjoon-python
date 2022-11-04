import sys
n = int(input())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
print(*a, sep='\n')
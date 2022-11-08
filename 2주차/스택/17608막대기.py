import sys
n = int(input())

stack = [int(sys.stdin.readline()) for _ in range(n)]
nstack = stack[::-1]

a = nstack[0]
count = 1

for i in range(1, len(nstack)):
    if a < nstack[i]:
        count += 1
        a = nstack[i]
        
print(count)
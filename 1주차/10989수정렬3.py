import sys
arr = [0] * 10001
n = int(input())
for i in range(n):
    a = int(sys.stdin.readline())
    arr[a] += 1
    
for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
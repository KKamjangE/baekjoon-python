import sys

# a = int(input().strip()[-1])
# arr = list(map(int, sys.stdin.readline().split()))
# for i in range(len(arr)):
#     if a > arr[i]:
#         print(arr[i], end=' ')

a, b = map(int, input().split())
print(*(t for t in map(int, input().split())if t < b))
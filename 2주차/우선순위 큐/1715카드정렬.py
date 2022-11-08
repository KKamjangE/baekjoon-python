import sys
import heapq

n = int(sys.stdin.readline()) # 카드 묶음 개수

arr = [] # 카드들의 크기를 넣은 배열
for _ in range(n):
    heapq.heappush(arr, int(sys.stdin.readline()))

ans = 0

if n == 1:
    ans = 0
else: # 묶음이 하나가 아니면
    while len(arr) > 1:
        tmp = heapq.heappop(arr) + heapq.heappop(arr) # 카드 묶음이 작은것 두개를 더함
        ans += tmp
        heapq.heappush(arr, tmp) # 더한 값을 다시 push
    
print(ans)
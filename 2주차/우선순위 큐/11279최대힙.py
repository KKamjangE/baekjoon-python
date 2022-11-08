import heapq
import sys

n = int(input())

arr = []

for i in range(n):
    a = int(sys.stdin.readline())
    
    if a == 0:
        if arr:
            hmax = heapq.heappop(arr) # 힙에서 제일 큰값 제거 후 저장
            print(-hmax) # 음수를 다시 양수로 바꿔서 출력
        else:
            print(0)
    else:
        heapq.heappush(arr, -a) # 받은 값 힙에 음수로 저장
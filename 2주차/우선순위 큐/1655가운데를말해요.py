import sys
import heapq

leftheap = [] # <= mid
rightheap = [] # > mid

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if len(leftheap) == len(rightheap): # 같으면 left부터 push 아니면 right push
        heapq.heappush(leftheap, (-x, x)) # heapq는 루트값을 min만 제공해주기 때문에 튜플로 음수값을 줌
    else:
        heapq.heappush(rightheap, (x, x))

    if rightheap and leftheap[0][1] > rightheap[0][0]: # right에 원소가 있고 left의 원래 값보다 right가 작으면
        min = heapq.heappop(rightheap)[0] # right에서 min원소
        max = heapq.heappop(leftheap)[1] # left에서 min원소의 원래 값
        heapq.heappush(leftheap, (-min, min)) # 교환
        heapq.heappush(rightheap, (max, max)) # 교환
            
    print(leftheap[0][1])
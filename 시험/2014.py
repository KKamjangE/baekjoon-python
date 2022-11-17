# 소수의 곱
# 답 보고 작성함
import sys
import heapq

k, n = map(int, sys.stdin.readline().split())
prime = list(map(int, sys.stdin.readline().split())) # 소수 배열

que = [] # 큐

for x in prime:
    heapq.heappush(que, x) # 소수 배열의 원소들 우선순위 큐로 정렬
    
for i in range(n): # 찾고자 하는 수 만큼 반복
    ans = heapq.heappop(que) # 결과값(우선순위 큐의 최소값)
    for j in range(k):
        nx = ans * prime[j] # 결과값과 소수배열의 값들 곱하기
        heapq.heappush(que, nx) # 곱한 값 다시 push
        if ans % prime[j] == 0: # 곱한 값이 중복 된다면 종료
            break

print(ans)
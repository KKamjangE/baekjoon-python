from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 동전 개수, 가치의 합
coins = set(int(input()) for _ in range(N)) # 

check = [0 for _ in range(K + 1)] # 동전 가치 리스트
que = deque()

for coin in coins: # 동전 마다
    if coin > K: # 동전이 가치의 합보다 클 경우
        continue # 다음 동전으로 넘어감
    que.append([coin, 1]) # 동전가치, 동전개수 push
    check[coin] = 1 # 해당 동전 개수 + 1 증가
    
flag  = True # 체크
while que: # 큐가 빌 때까지
    val, cnt = que.popleft() # 동전가치, 동전개수
    if val == K: # 동전 가치가 가치의 합과 동일하면
        print(cnt) # 동전개수 출력
        flag = False # 체크 처리
        break # 중지
    
    for coin in coins: # 동전 마다
        if val + coin > K: # 합친 동전 가치가 가치의 합보다 클 경우
            continue # 다음 동전으로 넘어감
        if check[val+coin] == 0: # 해당 가치가 비었다면
            check[val+coin] = 1 # 1로 체크
            que.append([val+coin, cnt + 1]) # 합친 동전 가치, 동전 개수 push

if flag:
    print(-1)
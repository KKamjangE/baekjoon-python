import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 동전 종류 개수, 만들어야 하는 금액

coins = [int(input()) for _ in range(N)] # 동전 종류 배열

coins.sort(reverse=True) # 내림차순으로 정렬

result = 0 # 동전 개수 카운팅

for coin in coins: # 큰 동전 부터
    if K == 0: # 만들어야 하는 금액이 충촉 됐다면
        break # 중지
    while coin <= K: # 동전이 금액보다 작을 때
        K -= coin # 금액 - 동전
        result += 1 # 동전 1개 추가
        
print(result)
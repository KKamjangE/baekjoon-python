import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

for _ in range(T): # 테스트 케이스 만큼
    N = int(input()) # 동전 종류 수
    coins = list(map(int, input().split())) # 동전 종류 리스트
    M = int(input()) # 만들어야 하는 금액
    
    num_arr = [0] * (M + 1) # 금액 종류 카운팅 리스트
    num_arr[0] = 1 # 0은 모든 동전으로 만들 수 있기에 1 저장
    for coin in coins: # 모든 종류의 동전 수행
        for i in range(1, M+1): # 금액이 만들어질 때까지
            if i >= coin: # 동전 금액보다 만들어야하는 금액이 클 경우
                num_arr[i] += num_arr[i-coin] # 전에 계산한 값에 더해서 만들 수 있는 경우의 수 +

    print(num_arr[M]) # 만들어야 하는 금액의 경우의 수
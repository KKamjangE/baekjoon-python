import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물건 개수, 배낭 무게 한도

knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)] # 그래프

arr = [list(map(int, input().split())) for _ in range(N)] # 물건의 종류 배열

print(*arr, sep='\n')
print(*knapsack, sep='\n')

for i in range(1, N + 1): # 물건의 개수만큼
    for j in range(1, K + 1): # 가방의 무게 만큼
        w = arr[i-1][0] # 물건 무게
        v = arr[i-1][1] # 물건 가치
        
        if j < w: # 가방에 물건이 안들어 가면
            knapsack[i][j] = knapsack[i - 1][j] # 전 물건의 가치 입력
        else: # 물건이 들어가면
            # max(현재 물건 가치 + 현재 물건의 무게를 뺀 지점의 물건의 가치, 이전 물건의 가치)
            knapsack[i][j] = max(v + knapsack[i - 1][j - w], knapsack[i - 1][j])

print(knapsack[N][K]) # 최종 가치 출력
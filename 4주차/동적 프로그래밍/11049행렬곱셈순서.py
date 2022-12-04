# pypy
import sys
input = sys.stdin.readline

N = int(input()) # 행렬 개수

arr = [list(map(int, input().split()))for _ in range(N)] # 행렬

dp = [[0]*N for _ in range(N)] # DP 그래프
# print(*arr, sep='\n')
# print(*dp, sep='\n')

for i in range(1, N): # 1 ~ N
    for j in range(N - i): # 0 ~ N - i
        x = j + i
        dp[j][x] = 2 ** 32 # 최대값
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + arr[j][0] * arr[k][1] * arr[x][1]) # 이전 계산값 + 행렬 곱 중에 작은 수
            
print(dp[0][N-1]) # 최종 최소값 출력
import sys
input = sys.stdin.readline

N = int(input()) # 수열의 크기 N
arr = list(map(int, input().split())) # 수열을 이루고 있는 원소

dp = [0 for _ in range(N)] # DP 테이블

for i in range(N): # 수열을 차례대로 비교하기 위한 for문
    for j in range(i): # 현재 원소의 이전 원소들을 비교하기 위한 for문
        if arr[i] > arr[j] and dp[i] < dp[j]: # 이전 원소보다 크고 테이블의 수열 길이가 더 짧을 때
            dp[i] = dp[j] # 이전 수열길이를 현재 수열길이로 갱신
    dp[i] += 1 # 수열길이 + 1
    
print(max(dp)) # 제일 긴 수열의 길이 출력
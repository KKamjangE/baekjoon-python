import sys
n = int(sys.stdin.readline()) # 수열의 개수

arr = list(map(int, sys.stdin.readline().split())) # 수열

dp = [0 for _ in range(n)] # 길이를 넣는 배열

for i in range(n): # index 차례대로
    for j in range(i): # 현재 index의 이전 수열들을 비교하기 위한 for문
        # 증가하는 수열인지 검사
        if arr[i] > arr[j] and dp[i] < dp[j]: # 이전 원소보다 현재 원소가 크고 저장된 길이값이 작을 경우
            dp[i] = dp[j] # 길이 복사
    # 모든 길이는 초기값이 0
    dp[i] += 1 # 길이 +
    
print(max(dp)) # 수열 중 가장 긴 길이를 출력
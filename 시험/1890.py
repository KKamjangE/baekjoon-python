# 점프
import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1 # 초기값 1

for x in range(N): # x 좌표
    for y in range(N): # y 좌표
        if x == N-1 and y == N-1: # 목적지 도착 체크
            print(dp[x][y]) # 목적지로 가는 경우의 수 출력
            break # 불필요한 연산 중지
            
        jump = board[x][y] # 점프 거리
        
        if x + jump < N: # x 좌표 점프 범위 체크
            dp[x+jump][y] += dp[x][y] # 현재 경우의 수 다음 위치에 +
            
        if y + jump < N: # y 좌표 점프 범위 체크
            dp[x][y+jump] += dp[x][y] # 현재 경우의 수 다음 위치에 +
            
# print(*dp, sep='\n')
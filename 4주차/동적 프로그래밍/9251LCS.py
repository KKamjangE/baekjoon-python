# LEC(Longest Common Subsequence) = 최장 공통 부분 수열
import sys
input = sys.stdin.readline

str_A = input().strip() # 문자열 A
str_B = input().strip() # 문자열 B

LCS = [[0]*(len(str_B) + 1) for _ in range(len(str_A) + 1)] # 문자열 비교 결과값 저장하는 그래프

for a in range(1, len(str_A) + 1):
    for b in range(1, len(str_B) + 1):
        if str_A[a-1] == str_B[b-1]: # 문자열A의 문자와 문자열B의 문자가 같다면
            LCS[a][b] = LCS[a - 1][b - 1] + 1 # 그 전에 비교했던 값을 참고하여 + 1
        else: # 다르다면
            LCS[a][b] = max(LCS[a - 1][b], LCS[a][b - 1]) # 그 전에 비교했던 값을 참고해서 더 큰값을 저장

# print(*LCS, sep='\n')
print(LCS[-1][-1]) # 모두의 부분 수열이 되는 수열 중 가장 긴 값을 찾아서 출력
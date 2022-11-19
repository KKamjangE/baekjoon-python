# LEC(Longest Common Subsequence) = 최장 공통 부분 수열
import sys
input = sys.stdin.readline

str_A = input().strip()
str_B = input().strip()

LCS = [[0]*(len(str_B) + 1) for _ in range(len(str_A) + 1)]

for a in range(1, len(str_A) + 1):
    for b in range(1, len(str_B) + 1):
        if str_A[a-1] == str_B[b-1]:
            LCS[a][b] = LCS[a - 1][b - 1] + 1
        else:
            LCS[a][b] = max(LCS[a - 1][b], LCS[a][b - 1])

print(*LCS, sep='\n')
print(LCS[-1][-1])
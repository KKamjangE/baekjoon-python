import sys
input = sys.stdin.readline

string_A = 'ABCDEF'
string_B = 'GBCDFE'
LCS = [[0] * (len(string_B) + 1) for _ in range(len(string_A) + 1)] # 문자열 비교 그래프 생성
# print(LCS)
for i in range(1, len(string_A) + 1):
    for j in range(1, len(string_B) + 1):
        # if i == 0 or j == 0: # 편의상 i, j가 0일때 0을 넣어줌
        #     LCS[i][j] = 0
        if  string_A[j - 1] == string_B[i - 1]: # 문자열 A, B의 한글자씩 비교
            LCS[i][j] = LCS[i - 1][j - 1] + 1 # 같다면 LCS[i-1][j-1]값을 찾아 + 1
        else:
            LCS[i][j] = 0 # 다르다면 LCS[i][j]에 0 표시
            
print(*LCS, sep='\n')
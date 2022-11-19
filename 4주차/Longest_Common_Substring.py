import sys
input = sys.stdin.readline

string_A = 'ABCDEF'
string_B = 'GBCDFE'
LCS = [[0] * (len(string_A)) for _ in range(len(string_B))]
# print(LCS)
for i in range(len(string_A)):
    for j in range(len(string_B)):
        # if i == 0 or j == 0: # 편의상 i, j가 0일때 0을 넣어줌
        #     LCS[i][j] = 0
        if  string_B[j] == string_A[i]: # 문자열 A, B의 한글자씩 비교
            LCS[i][j] = LCS[i - 1][j - 1] + 1 # 같다면 LCS[i-1][j-1]값을 찾아 + 1
        else:
            LCS[i][j] = 0 # 다르다면 LCS[i][j]에 0 표시
            
print(*LCS, sep='\n')
import sys

n = int(input()) # 종이의 길이

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 배열

result = [0, 0] # 결과값

def paper(n, x, y):
    color = arr[x][y] # 색상값 저장
    for i in range(x, x+n): # x좌표
        for j in range(y, y+n): # y좌표
            if color != arr[i][j]: # 다음 값이 저장한 색상과 다르다면
                paper(n//2, x, y) # 자르기
                paper(n//2, x, y+n//2)
                paper(n//2, x+n//2, y)
                paper(n//2, x+n//2, y+n//2)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

paper(n, 0, 0)
print(*result, sep='\n')
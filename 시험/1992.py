# 쿼드트리
import sys

n = int(sys.stdin.readline()) # 쿼드트리 길이

arr = [list(map(int, str(sys.stdin.readline().replace('\n', '')))) for _ in range(n)] # 쿼드트리 2차원 배열로 받기
ans = '' # 결과값

def quadTree(n, x, y):
    global ans
    boolean = arr[x][y] # 0, 0 위치의 원소 값 저장
    for i in range(x, x+n): # x 좌표 검사
        for j in range(y, y+n): # y 좌표 검사
            if boolean != arr[i][j]: # 저장해두었던 값과 다르면
                ans += '('
                # 4등분 재귀 호출
                quadTree(n//2, x, y)
                quadTree(n//2, x, y+n//2)
                quadTree(n//2, x+n//2, y)
                quadTree(n//2, x+n//2, y+n//2)
                ans += ')'
                return
    ans += str(boolean) # 0 or 1 저장
            
quadTree(n, 0, 0) # 쿼드트리 길이, x 좌표, y 좌표
print(ans)
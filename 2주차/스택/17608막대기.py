import sys
n = int(input())

stack = [int(sys.stdin.readline()) for _ in range(n)]
nstack = stack[::-1] # 역순 정렬

a = nstack[0] # 맨 앞의 원소
count = 1 # 결과값 첫번째 막대기는 무조건 보이기 때문에 1부터 시작

for i in range(1, len(nstack)):
    if a < nstack[i]: # 현재 원소보다 뒤의 원소가 클 경우
        count += 1
        a = nstack[i] # 현재 원소 변경
        
print(count)
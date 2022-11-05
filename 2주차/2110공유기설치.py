import sys

n, c = map(int, input().split())

arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
start, end = 1, arr[-1]-arr[0] # 거리 1 부터 최대 거리 8
while start <= end:
    mid = (start + end)//2 # 임의의 거리 중간으로 설정
    current = arr[0] # 현재 집 위치
    count = 1 # 공유기 갯수
    
    for i in range(1, len(arr)): # 2번 집부터 설치
        if arr[i] >= current + mid: # 현재 집부터 임의의 거리를 arr[i]의 집의 좌표와 비교
            count += 1 # 더 멀다면 공유기 설치
            current = arr[i] # 현재 집으로 변경
            
    if count >= c: # 설치가능한 공유기가 더 많으면
        start = mid + 1 # 거리를 더 넒힘
        ans = mid
    else: # 설치가능한 공유기가 더 적으면
        end = mid - 1 # 거리를 더 좁힘
        
print(ans)
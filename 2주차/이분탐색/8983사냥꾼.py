import sys

m, n, l = map(int, sys.stdin.readline().split()) # 사대 수, 동물 수, 사정거리
marr = list(map(int, sys.stdin.readline().split())) # 사대 위치
marr.sort() # 사대 정렬

count = 0 # 잡을 수 있는 동물 수
for i in range(n):
    a, b = map(int, sys.stdin.readline().split()) # 동물 위치
    left, right = 0, m-1 # 사대 좌표 배열을 기준을
    min = a + b - l # 사냥 가능한 최소 사대 좌표
    max = a - b + l # 사냥 가능한 최대 사대 좌표
    while left <= right:
        mid = (left + right) // 2 # 사대를 기준으로
        if marr[mid] <= max and marr[mid] >= min: # 사대의 사정거리 안에 들어온다면
            count += 1 # 사대 카운트
            break
        elif marr[mid] < max: # 사대위치 가 최대 사대 좌표보다 작다면
            left = mid + 1 # 사대 위치를 멀리
        else: # 사대위치가 가 최소 사대 좌표보다 작다면
            right = mid - 1 # 사대 위치를 적게
            
print(count)
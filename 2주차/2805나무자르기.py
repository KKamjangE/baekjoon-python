import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
bot, top = 1, max(arr) # 잘라야 하는 나무중 제일 긴 나무의 길이

while bot <= top:
    mid = (bot + top)//2 # 나무 가운데
    tree = 0 # 잘린 나무 길이의 합
    
    for a in arr:
        if a >= mid: # 자르는 부분보다 나무가 크면
            tree += a - mid # 잘라서 남은 부분 더하기
        
    if tree >= m: # 자른 나무들이 더 길다면
        bot = mid + 1 # 자르는 부분을 위쪽으로
    else: # 자른 나무가 부족하면
        top = mid - 1 # 자르는 부분을 아래쪽으로
            
print(top)
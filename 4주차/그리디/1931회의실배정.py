import sys
input = sys.stdin.readline

N = int(input()) # 회의 수

arr = [tuple(map(int, input().split())) for _ in range(N)] # 회의 시작시간, 끝나는 시간 저장

arr.sort(key=lambda x : (x[1], x[0])) # 회의 끝나는 시간 오름차순, 회의 시작시간 오름차순 정렬

end_time = arr[0][1] # 제일 먼저 시작해서 제일 빨리 끝나는 회의부터
ans = 1 # 이미 시작 회의가 1개 있어서 1부터 시작

for i in range(1, N):
    if end_time <= arr[i][0]: # 다음 회의 시작 시간이 현재 회의 끝나는 시간과 같거나 늦으면
        ans += 1 # 회의 수 + 1
        end_time = arr[i][1] # 회의 끝나는 시간 갱신
        
print(ans)
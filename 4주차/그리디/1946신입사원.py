import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수

for _ in range(T):

    N = int(input()) # 지원자 수
    arr = [list(map(int, input().split())) for _ in range(N)] # 서류심사 성적, 면접시험 성적 배열

    ans = 1 # 1등은 무조건 입사하기 때문에 1부터 시작
    arr.sort() # 서류심사 순위로 정렬
    top = arr[0][1] # 1등의 면접시험 성적

    for i in range(1, N):
        if top >= arr[i][1]: # 1등의 면접시험 성적보다 등수가 높다면
            ans += 1 # 입사 성공
            top = arr[i][1] # 해당 인원의 면접시험 성적으로 갱신

    print(ans) # 입사 인원 출력
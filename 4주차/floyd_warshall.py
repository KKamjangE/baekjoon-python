import sys
input = sys.stdin.readline

num = 4 # 전체 노드 개수
INF = int(1e9) # 무한대 값

# 자료 배열
arr = [[0, 5, INF, 8],
     [7, 0, 9, INF],
     [2, INF, 0, 4],
     [INF, INF, 3, 0]]

def floyd_warshall():
    ans_arr = [[0 for _ in range(num)] for _ in range(num)] # 결과 그래프 생성

    # 결과 그래프 초기화
    for arr_x in range(num): # x = 출발점
        for arr_y in range(num): # y = 목적지
            ans_arr[arr_x][arr_y] = arr[arr_x][arr_y]
            
    for middle in range(num): # 경유하는 노드
        for arr_x in range(num): # x = 출발점
            for arr_y in range(num): # y = 목적지
                if ans_arr[arr_x][middle] + ans_arr[middle][arr_y] < ans_arr[arr_x][arr_y]: # 경유해서 가는 가중치가 기존의 가중치보다 적다면
                    ans_arr[arr_x][arr_y] = ans_arr[arr_x][middle] + ans_arr[middle][arr_y] # 경유해서 가는 가중치로 갱신
                    
    print(*ans_arr, sep='\n') # 결과 그래프 출력
    
floyd_warshall()
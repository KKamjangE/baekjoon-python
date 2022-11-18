import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 다이나믹 프로그래밍
N = int(input()) # N번째 피보나치 수

fibonacci = [] # 연산한 값을 담을 배열
num = 0 # 연산값 저장할 변수
for i in range(N + 1): # 찾고자 하는 피보나치 수의 N번째만큼 반복
    if i == 0: # 0
        num = 0
    elif i <= 2: # 1 or 2
        num = 1
    else:
        num = fibonacci[-1] + fibonacci[-2] # 배열 맨 뒤의 첫번째와 두번째 값 연산
    fibonacci.append(num) # 연산한 값 리스트에 저장
    
print(fibonacci[-1]) # 최종 연산값 출력

# 재귀 방식
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
    
#     return f(n-1) + f(n-2)

# print(f(N))
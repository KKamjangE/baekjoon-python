import sys

input = sys.stdin.readline

N = int(input()) # 2진 수열의 길이

bin_arr = [] # 2진 수열 리스트
num = 0 # 연산 값

for i in range(1, N+1):
    if i == 1:
        num = i
    elif i == 2:
        num = i
    elif i == 3:
        num = i
    else:
        num = bin_arr[-1] + bin_arr[-2] # (N-1) + (N-2)
    
    bin_arr.append(num % 15746) # 15746으로 나눈 나머지 값 저장(여기서 나눠줘야 메모리 초과 안남)
    
print(bin_arr[-1]) # 맨 뒤의 원소 출력
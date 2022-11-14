import sys
input = sys.stdin.readline

def dfs(v, a, add, sub, mul, div):
    global maximum, minimum
    if v == N: # 수열의 길이와 같으면
        maximum = max(a, maximum) # 마지막 연산이 끝났을 때 max값인지 검사
        minimum = min(a, minimum) # 마지막 연산이 끝났을 때 min값인지 검사
        return

    # 해당 연산자가 존재한다면 v + 1, 현재 수열에 다음 수열 연산, 해당 연산자 - 1
    if add:
        dfs(v + 1, a + arr[v], add-1, sub, mul, div)
        
    if sub:
        dfs(v + 1, a - arr[v], add, sub-1, mul, div)

    if mul:
        dfs(v + 1, a * arr[v], add, sub, mul-1, div)

    if div:
        dfs(v + 1, int(a / arr[v]), add, sub, mul, div-1)
    
maximum = -1e9 # -1e9 = -10억
minimum = 1e9 # 1e9 = 10억

N = int(input()) # 수열 길이

arr = list(map(int, input().split())) # 수열 배열

add, sub, mul, div = map(int, input().split()) # 연산자 개수 정보 +, -, *, /

dfs(1, arr[0], add, sub, mul, div)
print(maximum)
print(minimum)
a, b, c = map(int, input().split())

def sol(a, b):
    if b == 1:
        return a % c
    else:
        tmp = sol(a, b // 2) # 지수 법칙과 분배 법칙으로 나눔
        if b % 2 == 0: # b가 2일때
            return(tmp * tmp) % c # 제곱
        else:
            return(tmp * tmp * a) % c # b가 홀수면 

print(sol(a, b))
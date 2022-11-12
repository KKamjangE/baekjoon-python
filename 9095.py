T = int(input())

def sum(n):
    if n == 1:
        return 1 # 받은 값이 1일 경우 1
    elif n == 2:
        return 2 # 받은 값이 2일 경우 2
    elif n == 3:
        return 4 # 받은 값이 3일 경우 4
    else:
        return sum(n-1)+sum(n-2)+sum(n-3) # 그 이상일 경우 n-1, n-2, n-3을 재귀 호출하여 합산
    
for _ in range(T):
    n = int(input())
    print(sum(n))
# 1000 이하의 소수를 나열하기(알고리즘 개선 1)

counter = 0 # 곱셈과 나눗셈 횟수를 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수를 저장하는 배열

prime[ptr] = 2 # 2는 소수
ptr += 1

prime[ptr] = 3 # 3은 소수
ptr += 1

for n in range(5, 1001, 2): # 홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <=n:
        counter += 2
        if n % prime[i] == 0: # 나누어 떨어지면 소수가 아님
            break # 반복 중단
        i += 1
    else: # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n # 소수로 배열에 등록
        ptr += 1
        counter += 1
        
for i in range(ptr): # ptr의 소수를 출력
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수{counter}')
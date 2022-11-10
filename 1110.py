N = int(input())
count = 0
n = N # n에 입력받은 값 저장
while True:
    a = n//10 # n의 앞자리수
    b = n%10 # n의 뒷자리수
    c = (a + b)%10 # a, b를 합한 수의 뒷자리수
    n = (b*10) + c # b를 앞자리수로 만들고 c를 더함
    count += 1
    if n == N:
        break
    
print(count)
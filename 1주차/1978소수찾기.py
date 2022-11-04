n = int(input())
arr = list(map(int, input().split()))
count = 0
for ar in arr: # 배열안에 요소 하나마다 적용
    for i in range(2, ar+1): # 2부터 요소의 숫자까지
        if ar%i == 0: # 2~요소 * 요소의 나머지가 0이 아니면
            if ar == i: # 위에 다 돌고 요소 = 요소면
                count += 1
            break
print(count)
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n-1

save = abs(arr[left] + arr[right]) # 첫번째와 마지막 값 합해서 저장
ans = [arr[left], arr[right]] # 정답

while left < right: # 좌우 포인터가 만날때 까지
    pl = arr[left] # 좌 포인터 값
    pr = arr[right] # 우 포인터 값

    sum = pl + pr # 좌우 포인터값을 합친 값 저장
    
    if abs(sum) < save: # 합친 절대값이 저장된 값보다 작으면
        save = abs(sum) # 합친 절대값을 저장
        ans = [pl, pr] # 정답에 저장
        if save == 0: # 저장해둔 값이 0이면 종료
            break
    if sum < 0: # 합친값이 0보다 작으면
        left += 1 # 좌 포인터 상승(양수 쪽으로)
    else:
        right -= 1 # 우 포인터 상승(음수 쪽으로)
        
print(ans[0], ans[1])
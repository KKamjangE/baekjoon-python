import sys
input = sys.stdin.readline

arr = input().strip().split('-') # '-'를 기준으로 나눠서 배열에 저장
ans = 0 # 결과값

for i in arr[0].split('+'): # 배열 첫번째 값을 '+'를 기준으로 나눈 원소들
    ans += int(i) # 결과값에 더해줌
    
for i in arr[1:]: # 배열의 첫번째 원소 이후의 원소들
    for j in i.split('+'): # 해당 원소를 '+'를 기준으로 나눈 원소들
        ans -= int(j) # 결과값에서 빼줌
        
print(ans)
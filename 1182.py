from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
a = len(arr)
count = 0

for i in range(1, len(arr)+1): # 1 ~ 원소 총 개수 까지
    comarr = list(combinations(arr, i)) # 부분 수열 구하기
    for ca in comarr:
        if sum(ca) == S: # 각 부분 수열의 합 비교
            count += 1
            
print(count)
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
ans = []

perarr = list(permutations(arr))

for per in perarr:
    count = 0
    for i in range(len(per)-1):
        count += abs(per[i]-per[i+1])
    ans.append(count)

print(max(ans))
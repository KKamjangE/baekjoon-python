import sys
c = int(input())
for i in range(c):
    arr = list(map(int, sys.stdin.readline().split()))
    count = 0
    for i in arr[1:]:
        if sum(arr[1:])/arr[0] < i:
            count += 1
    print(f'{count/arr[0]*100:.3f}%')
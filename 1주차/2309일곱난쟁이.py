import sys
arr = [int(sys.stdin.readline()) for _ in range(9)]
s = sum(arr)-100

for i in range(9):
    for j in range(i+1,9):
        if s == arr[i] + arr[j]:
            a, b = arr[i], arr[j]
            break
      
arr.remove(a)
arr.remove(b)
arr.sort()
print(*arr, sep='\n')
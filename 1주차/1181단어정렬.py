n = int(input())
arr = [input() for _ in range(n)]
result = list(set(arr))
result.sort()
result.sort(key=len)
print(*result, sep='\n')
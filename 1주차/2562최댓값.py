arr = [int(input())for _ in range(9)]
print(max(arr), arr.index(max(arr))+1, sep='\n')
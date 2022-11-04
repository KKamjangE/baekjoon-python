import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
arr = list(map(int, str(b)))
for i in range(len(arr)):
    print(arr[len(str(b))-1-i]*a)
print(a*b)
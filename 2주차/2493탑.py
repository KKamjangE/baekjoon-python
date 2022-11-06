n = int(input())

arr = list(map(int, input().split()))

stack = []
ans = []

for i in range(n):
    if stack:
        while stack:
            if stack [-1][1] < arr[i]:
                stack.pop() # pop
                if not stack:
                    ans.append(0) # ans
                    stack.append([i, arr[i]]) # push
                    break
            else:
                ans.append(stack[-1][0]+1) # ans
                stack.append([i, arr[i]]) # push
                break
    else:
        ans.append(0) # ans
        stack.append([i, arr[i]]) # push

print(*ans, sep=' ')
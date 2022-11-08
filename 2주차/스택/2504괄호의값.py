import sys

arr = sys.stdin.readline()

stack = [] # 스택
ans = 0
tmp = 1 # 미리 곱한 값

for i in range(len(arr)): # index 순서대로
    if arr[i] == '(':
        stack.append(arr[i])
        tmp *= 2 # tmp에 미리 2를 곱함 (한번 더 열리면 자동으로 곱해짐)
    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *= 3 # tmp에 미리 3을 곱함 (한번 더 열리면 자동으로 곱해짐)
    elif arr[i] == ')':
        if not stack or stack[-1] == '[': # stack이 비었거나 top이 '['면
            ans = 0
            break
        if arr[i-1] == '(': # 이전 값이 '('면
            ans += tmp # 2 더하기
        stack.pop() # pop
        tmp //= 2 # 미리 곱했던 값 다시 나눠서 원래대로
    elif arr[i] == ']':
        if not stack or stack[-1] == '(': # stack이 비었거나 top이 '('면
            ans = 0
            break
        if arr[i-1] == '[': # 이전 값이 '['면
            ans += tmp # 3 더하기
        stack.pop() # pop
        tmp //= 3 # 미리 곱했던 값 다시 나눠서 원래대로
        
if stack:
    print(0) # stack이 남았으면 0
else:
    print(ans) # stack이 비었으면 값 출력
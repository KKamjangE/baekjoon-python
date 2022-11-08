from collections import deque
import sys

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    n = arr.pop(0)
    
    if n == 0:
        break
    
    stack = deque()
    ans = 0
    
    for i in range(n): # 인덱스 순으로 탐색
        while len(stack) != 0 and arr[stack[-1]] > arr[i]: # stack이 비어있지 않거나 stack의 top 값이 현재 값보다 클 경우
            tmp = stack.pop() # tmp에 stack의 top 값 pop해서 저장
            
            if len(stack) == 0: # stack이 비었을 경우
                w = i # 넓이는 현재 탑의 인덱스 값
            else:
                w = i - stack[-1] - 1 # stack이 비어있지 않다면 이어진다는 뜻(넓이 늘어남)
            ans = max(ans, w * arr[tmp]) # 저장된 값과 넓이 * tmp에 인덱스 직사각형의 값 비교해서 큰거 저장
        stack.append(i) # stack이 비었을 경우 push
        
    while len(stack) != 0: # stack에 남은 원소 처리
        tmp = stack.pop()
        
        if len(stack) == 0:
            w = n # n인 이유는 마지막 인덱스 +1 이기 때문에
        else:
            w = n - stack[-1] - 1 # stack이 비어있지 않다면 이어진다는 뜻(넓이 늘어남)
        ans = max(ans, w * arr[tmp]) # 저장된 값과 넓이 * tmp에 인덱스 직사각형의 값 비교해서 큰거 저장
        
    print(ans)
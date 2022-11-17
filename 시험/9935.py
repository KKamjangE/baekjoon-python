# 문자열 폭발
import sys

arr = sys.stdin.readline().replace('\n', '') # 문자열
x = sys.stdin.readline().replace('\n', '') # 폭발 문자열

stack = []

for a in arr:
    stack.append(a)
    cnt = 0
    # stack의 top원소가 폭발 문자열 맨뒤 원소와 같고 stack이 폭발 문자열 보다 길 경우
    if stack[-1] == x[-1] and len(stack) >= len(x):
        # stack과 폭발 문자열이 모두 동일한지 비교
        for i in range(1, len(x)+1):
            if stack[-i] == x[-i]:
                cnt += 1 # 동일할 때 마다 count ++
            else:
                break
        if cnt == len(x): # count가 폭발 문자열의 길이와 동일하다면
            for _ in range(cnt): # 문자열 폭발
                stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')
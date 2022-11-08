import sys
rank = { # 연산자 우선순위 지정
    '*': 3, '/': 3, '+': 2, '-': 2, '(': 1
}
stack = [] # 스택 생성
infix = sys.stdin.readline().replace('\n', '').replace(' ', '') # infix 입력
ans = ''

for w in infix: # infix postfix로 변환
    if w in rank: # 연산자인지 확인
        if not stack: # stack이 비었다면
            stack.append(w) # push
        else:
            if w == '(': # '('면
                stack.append(w) # push
            else:
                while rank.get(w) <= rank.get(stack[-1]): # 입력받은 연산자와 stack안의 연산자 우선순위 비교
                    ans += stack.pop() # ans += pop
                    if len(stack) == 0: # stack이 비었다면 종료
                        break
                stack.append(w) # push
    elif w == ')': # ')'면
        while stack[-1] != '(': # '('만 stack에 남을 때 까지
            ans += stack.pop() # ans += pop
        stack.pop() # '(' pop
    else: # 피연산자면
        ans += w # ans +=
while stack: # stack에 남은 연산자들 처리
    ans += stack.pop() # ans += pop
print(f'postfix : {ans}')

for a in ans: # postfix 계산
    if a == '+':
        stack.append(stack.pop() + stack.pop()) # stack 원소 pop하고 연산해서 다시 push
    elif a == '-':
        stack.append(stack.pop() - stack.pop()) # stack 원소 pop하고 연산해서 다시 push
    elif a == '*':
        stack.append(stack.pop() * stack.pop()) # stack 원소 pop하고 연산해서 다시 push
    elif a == '/':
        stack.append(stack.pop() / stack.pop()) # stack 원소 pop하고 연산해서 다시 push
    else:
        stack.append(int(a)) # 피연산자 push

print(f'result : {stack.pop()}')
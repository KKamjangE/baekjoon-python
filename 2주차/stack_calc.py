import sys
rank = {
    '*': 3, '/': 3, '+': 2, '-': 2, '(': 1
}
stack = []
infix = sys.stdin.readline().replace('\n', '').replace(' ', '')
ans = ''

for w in infix:
    if w in rank:
        if not stack:
            stack.append(w)
        else:
            if w == '(':
                stack.append(w)
            else:
                while rank.get(w) <= rank.get(stack[-1]):
                    ans += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(w)
    elif w == ')':
        while stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    else:
        ans += w
while stack:
    ans += stack.pop()
print(f'postfix : {ans}')

for a in ans:
    if a == '+':
        stack.append(stack.pop() + stack.pop())
    elif a == '-':
        stack.append(stack.pop() - stack.pop())
    elif a == '*':
        stack.append(stack.pop() * stack.pop())
    elif a == '/':
        stack.append(stack.pop() / stack.pop())
    else:
        stack.append(int(a))

print(f'result : {stack.pop()}')
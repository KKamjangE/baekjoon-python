# 배열을 이용한 심플 스택 구현

stack = []

def push(x: int):
    stack.append(x)

def pop():
    if stack:
        stack.pop()
    else:
        return print('스택이 비었습니다.')

def top():
    if stack:
        return print(stack[-1])
    else:
        return print('스택이 비었습니다.')
    
def size():
    return print(len(stack))

def empty():
    if stack:
        return print(False)
    else:
        return print(True)

n = int(input('명령횟수를 입력: ')) # 명령 개수
for i in range(n):
    a = input('명령을 입력(push, pop, top, size, empty): ')
    if a == 'push':
        x = int(input('push 값 입력: '))
        push(x)
    elif a == 'pop':
        pop()
    elif a == 'top':
        top()
    elif a == 'size':
        size()
    elif a == 'empty':
        empty()
    else:
        print('입력 오류')
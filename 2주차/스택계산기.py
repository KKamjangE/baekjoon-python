import sys

prec = { # 연산자 우선순위 부여
    '*': 3, '/': 3, '+': 2, '-': 2, '(': 1
}

class ArrayStack:
    
    def __init__(self) -> None: # stack 생성
        self.data = []
        
    def size(self) -> int: # stack 사이즈
        return len(self.data)
    
    def isEmpty(self) -> bool: # stack이 비었는가?
        return self.size() == 0
    
    def push(self, item) -> None: # 데이터 추가
        self.data.append(item)
        
    def pop(self) -> None: # 데이터 삭제
        return self.data.pop()
    
    def peek(self) -> int: # 맨 앞의 원소값
        return self.data[-1]
    
def convert_to_postfix(S): # postfix로 전환하는 함수
    opStack = ArrayStack() # 스택 생성
    answer = '' # 전환한 값 저장소
    
    for w in S:
        if w in prec: # 받은 값이 연산자인지 확인
            if opStack.isEmpty(): # 스택이 비어있다면
                opStack.push(w) # 받은값 바로 push
            else:
                if w == '(': # 여는괄호면
                    opStack.push(w) # 바로 push
                else:
                    while prec.get(w) <= prec.get(opStack.peek()): # 들어온 값의 우선순위와 stack 맨앞 원소의 우선순위 비교
                        answer += opStack.pop() # 우선순위가 낮다면 stack에 있던 값 pop하고 전환에 저장
                        if opStack.isEmpty(): break # stack이 비면 종료
                    opStack.push(w) # 우선순위가 높다면 저장
        elif w == ')': # 닫는 괄호면
            while opStack.peek() != '(': # 맨 앞 원소가 여는 괄호만 남을때까지
                answer += opStack.pop() # stack에 있던 값 pop하고 전환값에 저장
            opStack.pop() # 여는 괄호 pop
        else :
            answer += w # 피연산자면 전환값에 저장
    
    while not opStack.isEmpty(): # stack이 빌때까지
        answer += opStack.pop() # stack에 있던 값 pop하고 전환값에 저장
    
    return answer # 전환값 리턴

def calculate(tokens): # 계산 함수
    stack = ArrayStack() # 스택 생성
    for token in tokens:
        if token == '+':
            stack.push(stack.pop()+stack.pop()) # stack 안의 두값 연산
        elif token == '-':
            stack.push(-(stack.pop()-stack.pop())) # stack 안의 두값 연산
        elif token == '*':
            stack.push(stack.pop()*stack.pop()) # stack 안의 두값 연산
        elif token == '/':
            rv = stack.pop()
            stack.push(stack.pop()/rv) # stack 안의 두값 연산
        else:
            stack.push(int(token)) # 피연산자는 stack에 바로 push
    return stack.pop()

infix = sys.stdin.readline().replace("\n", "").replace(" ","")

postfix = convert_to_postfix(infix)

print(f"postfix : {postfix}")

result = calculate(postfix)

print(f"result : {result}")
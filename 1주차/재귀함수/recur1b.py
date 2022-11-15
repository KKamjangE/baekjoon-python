# [Do it! 실습 5-5] 스택으로 재귀 함수 구현하기(재귀를 제거)

from stack import Stack  # stack.py의 Stack 클래스를 임포트

def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            # n값 4를 스택에 푸시
            s.push(n)         # n 값을 푸시
            # n을 1 감소시켜 3으로 만듬
            n = n - 1
            # countinue문이 실행되어 while문으로 돌아감
            continue
        if not s.is_empty():  # 스택이 비어 있지 않으면
            # 스택에서 팝한 값 1을 n으로 꺼냄
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            # n값 1출력
            print(n)
            # n값을 2감소시켜 -1로 합니다
            n = n - 2
            # countinue문의 동작으로 while문 맨 앞으로 돌아감
            continue
        break

x = int(input('정수값을 입력하세요.: '))

recur(x)
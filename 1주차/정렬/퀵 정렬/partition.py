# 배열을 두 그룹으로 나누기

from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """배열을 분할하여 출력"""
    n = len(a)
    pl = 0         # 왼쪽 커서
    pr = n - 1     # 오른쪽 커서
    x = a[n // 2]  # 피벗(가운데 원소)

    while pl <= pr: # 둘이 교차하기 전까지 실행
        while a[pl] < x: pl += 1 # 피벗보다 작은걸 찾을때까지 +해서 뒤로
        while a[pr] > x: pr -= 1 # 피벗보다 큰걸 찾을때까지 -해서 앞으로
        if pl <= pr: # 검색해서 나온애들 비교
            a[pl], a[pr] = a[pr], a[pl] # 자리 교체
            pl += 1 # 다음 찾기
            pr -= 1 # 다음 찾기

    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')
    print(*a[0 : pl])           # a[0] ~ a[pl - 1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl])  # a[pr + 1] ~ a[pl - 1]

    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1 : n])       # a[pr + 1] ~ a[n - 1]

if __name__ == '__main__':
    print('배열을 나눕니다.')  
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)         # 배열 x를 나누어서 출력
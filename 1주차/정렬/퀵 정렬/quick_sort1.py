# 퀵 정렬 알고리즘 구현하기

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left # 왼쪽 커서
    pr = right # 오른쪽 커서
    x = a[(left + right) // 2]   # 피벗(가운데 원소)

    print(f'a[{left}] ~ a[{right}]:', *a[left : right + 1])

    while pl <= pr: # 둘이 교차하기 전까지 실행
        while a[pl] < x: pl += 1 # 피벗보다 작은걸 찾을때 까지 +해서 뒤로 이동
        while a[pr] > x: pr -= 1 # 피벗보다 큰걸 찾을때 까지 -해서 앞으로 이동
        if pl <= pr: # 검색해서 나온 결과 비교
            a[pl], a[pr] = a[pr], a[pl] # 자리 교체
            pl += 1 # 다음 찾기
            pr -= 1 # 다음 찾기
            
    if left < pr: qsort(a, left, pr) # 나눈 왼쪽 그룹의 인덱스 left~pr값으로 다시 나눔
    if pl < right: qsort(a, pl, right) # 나눈 오른쪽 그룹의 인덱스 pl~rigit값으로 다시 나눔
    
def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)
    
if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num # 원소 수가 num인 배열 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    quick_sort(x) # 배열 x를 퀵 정렬
    
    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
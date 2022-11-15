# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1, n): # 1~ 배열의 끝까지
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp: # j가 0번인덱스(끝)에 도달하거나 tmp가 앞쪽 원소보다 작으면
            a[j] = a[j - 1] # 앞쪽원소를 현재 원소에 대입
            j -= 1 # -1하면서 점점 앞쪽으로
        a[j] = tmp # 현재 자리에 대입

if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num # 원소 수가 num인 배열을 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    insertion_sort(x) # 배열 x를 단순 삽입 정렬
    
    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
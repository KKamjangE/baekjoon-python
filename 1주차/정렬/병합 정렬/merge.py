# 정렬을 마친 두 배열을 병합하기

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0                 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c)  # 각 배열의 원소수 

    while pa < na and pb < nb:  # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]: # a가 b보다 작으면
            c[pc] = a[pa] # c에 a저장
            pa += 1 # a의 인덱스 1증가
        else:
            c[pc] = b[pb] # c에 b저장
            pb += 1 # b의 인덱스 1증가
        pc += 1 # 둘중 하나의 값이라도 넣었으니 c의 인덱스 1증가

    while pa < na:              # a에 남은 원소를 복사 a의 길이까지 반복
        c[pc] = a[pa] # a에 데이터 c에 저장
        pa += 1 # a의 인덱스 1증가
        pc += 1 # c의 인덱스 1증가

    while pb < nb:              # b에 남은 원소를 복사
        c[pc] = b[pb] # b에 데이터 c에 저장
        pb += 1 # b의 인덱스 1증가
        pc += 1 # c의 인덱스 1증가

if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13] # 이미 정렬을 마친 a배열
    b = [1, 2, 3, 4, 9, 16, 21] # 이미 정렬을 마친 b배열
    c = [None] * (len(a) + len(b)) # a와 b의 길이를 더한 만큼의 길이의 원소값이 없는 c배열 생성
    print('정렬을 마친 두 배열의 병합을 수행합니다.')

    merge_sorted_list(a, b, c)  # 배열 a와 b를 병합하여 c에 저장

    print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')
# 병합 정렬 알고리즘 구현하기

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right)       # 배열 뒷부분을 병합 정렬

            p = j = 0
            i = k = left

            while i <= center: # 배열a의 앞부분 모두 버퍼에 임시 저장
                 buff[p] = a[i] # 임시 저장
                 p += 1
                 i += 1

            while i <= right and j < p:
                 if buff[j] <= a[i]: # 복사한 버퍼배열과 남아있는 a의 center부터 끝까지의 원소를 비교
                     a[k] = buff[j] # 버퍼[0] 저장한 값이 작으면 a[0~]에 저장 (a[0]은 이미 버퍼에 저장해놔서)
                     j += 1 # 버퍼 배열 인덱스 증가
                 else:
                     a[k] = a[i] # 배열 a의 center부터 a[0~]배열에 저장
                     i += 1 # a[i~+]
                 k += 1 # a[k~+]

            while j < p: # 버퍼에 남은 원소들 a[k]에 대입하기
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1)    # 배열 전체를 병합 정렬 배열a와 인덱스 0번~마지막
    del buff                    # 작업용 배열을 소멸

if __name__ == '__main__':
    print('병합 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)       # 배열 x를 병합 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
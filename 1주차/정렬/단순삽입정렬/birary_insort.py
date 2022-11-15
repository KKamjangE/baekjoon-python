# 이진 삽입 정렬 알고리즘 구현(bisect.insort 사용)

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬(binary_insort 사용)"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
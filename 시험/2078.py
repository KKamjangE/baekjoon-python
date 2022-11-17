# 무한이진트리
# pypy 제출

import sys
input = sys.stdin.readline
L, R = map(int, input().split()) # 찾아야 하는 노드 위치

left, right = 0, 0

while L != 1 or R != 1: # 좌, 우가 1이 되어 루트가 될 때까지
    if L > R: # 왼쪽이 오른쪽보다 크다면
        L -= R # 왼쪽에서 오른쪽을 -
        left += 1 # 왼쪽 + 1
    else: # 오른쪽이 더 크다면
        R -= L # 오른쪽에서 왼쪽을 -
        right += 1 # 오른쪽 + 1
        
print(left, right)
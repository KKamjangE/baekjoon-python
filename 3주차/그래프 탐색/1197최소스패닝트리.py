import sys

v, e = map(int, sys.stdin.readline().split()) # 정점의 개수, 간선의 개수

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split()) # a정점과 b정점이 가중치 c인 간선으로 연결
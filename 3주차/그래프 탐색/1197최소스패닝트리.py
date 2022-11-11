import sys

def find_parent(parent, x): # 집합의 부모 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # 더 작은 값을 부모 노드로 설정
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, sys.stdin.readline().split()) # 정점의 개수, 간선의 개수
parent = [0] * (v + 1) # 부모 배열 생성

for i in range(1, v+1):
    parent[i] = i # 본인의 값을 부모로 초기화

edges = [] # 정점, 간선 배열

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split()) # a정점과 b정점이 가중치 c인 간선으로 연결
    edges.append([cost, a, b]) # 2차원 배열로 생성

edges.sort() # 정렬
result = 0 # 결과값

for edge in edges: # 각각 한번씩
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # 부모 노드가 동일한지 검사
        union_parent(parent, a, b) # 다르다면 합치기
        result += cost # cost증가  
        
print(result)
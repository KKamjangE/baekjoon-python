import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input()) # 테스트 케이스의 개수

def dfs(v, group): # DFS, (group은 체크용 1 or -1)
    visit[v] = group # 그룹 부여
    for i in g[v]:
        if not visit[i]: # 방문 체크
            chk = dfs(i, -group) # chk에 bool값 저장
            if not chk: # False면
                return False # False 반환
        elif visit[i] == visit[v]: # 인접한 노드와 동일하다면
            return False # False 반환
    return True # 문제 없으면 True 반환


for _ in range(k):
    V, E = map(int, input().split()) # 정점 수, 간선 수
                
    g = [[]for _ in range(V + 1)] # 빈 인접 리스트

    visit = [False] * (V+1) # 방문 리스트

    for _ in range(E): # 인접 리스트에 간선 입력
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    
    for i in range(1, V + 1): # 그래프가 하나가 아닐 경우 때문에 한번씩 다 확인
        if not visit[i]: # 방문 체크
            result = dfs(i, 1)
            if not result:
                break
        
    print('YES' if result else 'NO')
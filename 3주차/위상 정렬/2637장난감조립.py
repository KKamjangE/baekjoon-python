from collections import deque
import sys
input = sys.stdin.readline

def default_part(part): # 진입 차수가 0 인지 확인
    for i in range(0, N):
        if parts[part][i] != 0: # 진입 차수가 하나라도 존재한다면
            return False
    return True

N = int(input().strip()) # 완제품 번호

M = int(input().strip()) # 부품 관계 수

que = deque() # 큐 데크 생성

parts = [[0] * (N + 1) for _ in range(N + 1)] # 각 부품을 만들때 필요한 부품

g = [[] for _ in range(N + 1)] # 인접 리스트
inDegree = [0 for _ in range(N + 1)] # 진입 차수 리스트

for _ in range(M): # 인접 리스트 생성
    a, b, x = map(int, input().split()) # 간선 a, b, 가중치 x
    g[b].append((a, x)) # 목적지에 출발지와 가중치 저장
    inDegree[a] += 1 # 진입 차수 + 1
    
for i in range(1, N + 1):
    if inDegree[i] == 0: # 진입 차수가 0이면 시작점
        que.append(i)
    
while que: # 큐가 빌 때까지
    node = que.popleft() # 현재 노드
    for next, need_parts in g[node]: # 현재 노드의 간선만큼 목적지, 가중치
        if default_part(node): # 현재 노드에 진입차수가 없다면 
            parts[next][node] += need_parts # 목적지에 가중치 저장
        else:
            for i in range(1, N + 1):
                parts[next][i] += parts[node][i] * need_parts # 현재 부품을 만드는데 필요 부품 * 다음 부품의 필요 수

        inDegree[next] -= 1 # 진입차수 제거 -1

        if inDegree[next] == 0: # 진입 차수가 없다면
            que.append(next) # 큐에 push
        
for i in range(1, N):
    if parts[N][i] != 0: # 완제품 배열에서 0이 아닌것만 출력
        print(i, parts[N][i])
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

que = deque() # 큐 데크 생성
g = [[]for _ in range(N + 1)] # 인접 리스트
inDegree = [0 for _ in range(N + 1)] # 진입차수 리스트

for _ in range(M): # 인접 리스트 생성
    a, b = map(int, input().split())
    g[a].append(b) # 간선 입력
    inDegree[b] += 1 # 목적지에 진입차수 + 1
    
for i in range(1, N+1):
    if inDegree[i] == 0: # 진입차수가 0인 경우
        que.append(i) # 큐에 push
        
ans = []

while que:
    node = que.popleft() # node에 진입차수가 0인(시작점) 저장
    ans.append(node) # 결과값에 저장
    for i in g[node]: # 해당 노드가 가지고 있는 간선만큼
        inDegree[i] -= 1 # 차수 제거 
        if inDegree[i] == 0: # 차수가 0개면
            que.append(i) # 해당 노드 큐에 push
            
print(*ans)
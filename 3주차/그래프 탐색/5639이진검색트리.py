# DFS
import sys
sys.setrecursionlimit(10**8) # 재귀 호출 깊이 제한
arr = []
while True:
    try:
        arr.append(int(sys.stdin.readline())) # 전위 순회값 입력
    except: # 예외 발생시 입력 중단
        break
    
def postorder(start, end): # 후위 순회
    if start > end: # root가 넘어가면 종료
        return
    
    idx = end + 1 # 한쪽 자식이 아예 없다는 예외를 대비
    root = arr[start] # 루트 노드
    
    for i in range(start+1, end+1):
        if root < arr[i]: # 루트값 보다 크면 오른쪽이라는 뜻
            idx = i # 멈춘 구간에 index값 저장
            break
        
    postorder(start+1, idx-1) # 왼쪽 서브 트리
    postorder(idx, end) # 오른쪽 서브 트리
    print(root) # 현재 루트값 출력

postorder(0, len(arr)-1)
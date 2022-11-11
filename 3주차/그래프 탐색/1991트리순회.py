import sys

n = int(sys.stdin.readline()) # 트리 레벨

tree = {} # 딕셔너리

for i in range(n): # 레벨 만큼
    root, left, right = sys.stdin.readline().split() # 루트, 왼쪽 자식, 오른쪽 자식
    tree[root] = left, right # 루트를 키로 자식들을 값으로 설정해서 딕셔너리에 저장
    
def preorder(root): # 전위 순회(루트 -> 왼쪽 -> 오른쪽)
    if root != '.': # 리프가 아닐 경우
        print(root, end='') # 루트
        preorder(tree[root][0]) # 루트의 왼쪽
        preorder(tree[root][1]) # 루트의 오른쪽

def inorder(root): # 중위 순회(왼쪽 -> 루트 -> 오른쪽)
    if root != '.': # 리프가 아닐 경우
        inorder(tree[root][0]) # 루트의 왼쪽
        print(root, end='') # 루트
        inorder(tree[root][1]) # 루트의 오른쪽

def postorder(root): # 후위 순회(왼쪽 -> 오른쪽 -> 루트)
    if root != '.': # 리프가 아닐 경우
        postorder(tree[root][0]) # 루트의 왼쪽
        postorder(tree[root][1]) # 루트의 오른쪽
        print(root, end='') # 루트
        
preorder('A') # 전위 순회 루트 A
print()
inorder('A') # 중위 순회 루트 A
print() 
postorder('A') # 후위 순회 루트 A
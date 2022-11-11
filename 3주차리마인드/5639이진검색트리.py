import sys
sys.setrecursionlimit(10**8)

arr = []

while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break
    
def postorder(start, end):
    if start > end:
        return
    
    mid = end + 1
    root = arr[start]
    
    for i in range(start + 1, end + 1):
        if root < arr[i]:
            mid = i
            break
        
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)
    
postorder(0, len(arr)-1)
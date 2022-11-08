a = int(input())
arr = list(map(int, input().split()))
n = int(input())
chk = list(map(int, input().split()))
arr.sort()
def search(a, key):
    
    pl = 0
    pr = len(a)-1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

for i in range(len(chk)):
    print(search(arr, chk[i]))
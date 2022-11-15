# 퀵 정렬 만들어보기

a = [3, 1, 2, 5, 3, 1]

def quick(a, left, right):
    pr = right
    pl = left
    x = a[(left + right)//2]
    
    while pl<=pr:
        while a[pl]<x:
            pl += 1
        while a[pr]>x:
            pr -= 1
        
        if left <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        quick(a, left, pr)
        quick(a, pl, right)
      
quick(a, 0, 5)      
print(*a)
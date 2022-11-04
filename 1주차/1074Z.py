a, x, y = map(int, input().split())

def Z(a, x, y):
    if a == 0:
        return 0
    return 2*(x%2)+(y%2) + 4 * Z(a-1, int(x/2), int(y/2))

print(Z(a, x, y))
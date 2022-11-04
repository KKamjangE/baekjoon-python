import sys
a = int(input())
for i in range(a):
    score = 0
    total = 0
    ox = sys.stdin.readline().strip()
    for j in range(len(ox)):
        if ox[j] == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)
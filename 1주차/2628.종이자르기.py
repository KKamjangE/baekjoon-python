y, x = map(int, input().split())
ga = [0, x]
se = [0, y]
maxga = []
maxse = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0:
        ga.append(b)
    else:
        se.append(b)

ga.sort()
se.sort()

for i in range(len(ga)-1):
    maxga.append(ga[i + 1] - ga[i])
    
for i in range(len(se)-1):
    maxse.append(se[i + 1] - se[i])

print(max(maxga) * max(maxse))
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

adaptor = list(map(int, input().split()))

ans = 0
length = []
scheduling = []
for i in range(N):
    scheduling.append(adaptor[i])

end = 0
for i in range(N):
    if scheduling in adaptor[i]:
        end += 1
    else:
        break
    
for next_idx in range(end, K):
    if adaptor[next_idx] in scheduling:
        length.append(next_idx)
        

print(ans)
# print(adaptor)
# print(scheduling)
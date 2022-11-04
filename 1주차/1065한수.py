n = int(input())

count = 0
for i in range(1, n+1):
    arr = list(map(int, str(i))) # 1~n까지의 수를 str으로 배열화
    if i < 100:
        count += 1 # 100보댜 작으면 한수
    elif arr[0]-arr[1] == arr[1]-arr[2]:
        count += 1 # x의 각 자리가 등차수열이면 한수
print(count)
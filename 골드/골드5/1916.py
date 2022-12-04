# 폴로이드 워샬 - 시간초과
n = int(input())
m = int(input())
arr = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i][i] = 0

for i in range(m):
    x, y, z = map(int, input().split())
    arr[x][y] = z

p_x, p_y = map(int, input().split())

for i in range(1, n + 1):
    for j in  range(1, n + 1):
        for k in range(1, n + 1):
            arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

print(arr[p_x][p_y])
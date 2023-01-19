# 플로이드 워샬
n = int(input())
m = int(input())
inf = 2147000000
arr = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
    
for i in range(n):
    arr[i][i] = 0
    for j in range(n):
        for k in range(n):
            arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i][j] == inf and arr[j][i] == inf:
            count += 1
    print(count)
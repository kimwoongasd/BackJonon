import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 2147000000
arr = [[inf] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a - 1][b - 1] = min(c, arr[a-1][b-1])

for i in range(n):
    arr[i][i] = 0
    for j in range(n):
        for k in range(n):
            arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

for x in arr:
    for j in x:
        if j == inf:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()
n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif j == i:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

print(max(arr[n - 1]))
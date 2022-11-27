t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(2):
        a = list(map(int, input().split()))
        arr.append(a)
    
    for i in range(1, n):
        if i == 1:
            arr[0][i] += arr[1][i - 1]
            arr[1][i] += arr[0][i - 1]
        else:
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])

    print(max(arr[0][n - 1], arr[1][n - 1]))
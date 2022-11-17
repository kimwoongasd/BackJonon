n = int(input())
arr = list(map(int, input().split()))
ch = [0] * n
ch[0] = arr[0]

for i in range(1, n):
    t = 0
    for j in range(i, -1, -1):
        if arr[i] > arr[j] and ch[j] > t:
            t = ch[j]
    ch[i] = t + arr[i]

print(max(ch))
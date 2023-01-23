n = int(input())
arr = list(map(int, input().split()))
ch = [0] * n
ch[0] = 1
for i in range(1, n):
    tem = 0
    for j in range(i, -1, -1):
        if arr[i] > arr[j] and ch[j] > tem:
            tem = ch[j]
    ch[i] = tem + 1
print(max(ch))
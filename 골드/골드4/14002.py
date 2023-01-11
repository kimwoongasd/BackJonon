n = int(input())
arr = list(map(int, input().split()))

ch = [0] * n
ch[0] = 1
num = [[arr[0]]]
for i in range(1, n):
    m = 0
    tem = []
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and ch[j] > m:
            m = ch[j]
            tem = num[j]
    ch[i] = m + 1
    num.append(tem + [arr[i]])
 
print(max(ch))
for x in num:
    if len(x) == max(ch):
        print(*x)
        break
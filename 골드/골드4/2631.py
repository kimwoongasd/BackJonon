# 힌트롤 보고 dp로 풀려했으나 못품
# LIS (가장긴 부분수열) 문제를 보고폼
n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

ch = [0] * n
ch[0] = 1
for i in range(1, n):
    tem = 0
    for j in range(i, -1, -1):
        if arr[i] > arr[j] and ch[j] > tem:
            tem = ch[j]
    ch[i] = tem + 1

print(n - max(ch))
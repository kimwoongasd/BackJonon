n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

s = 0
e = 0
res = 2147000000
while s < n and e < n:
    total = arr[e] - arr[s]
    if m > total :
        e += 1
    else:
        s += 1
        res = min(total, res)

print(res)
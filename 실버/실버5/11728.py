n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
e = 0
res = []
while s < n and e < m:
    if a[s] >= b[e]:
        res.append(b[e])
        e += 1
    else:
        res.append(a[s])
        s += 1

if s == n:
    for i in range(e, m):
        res.append(b[i])
else:
    for i in range(s, n):
        res.append(a[i])
print(*res)
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = dict()
for i in range(n):
    d[a[i]] = d.get(a[i], 0) + 1
for i in range(m):
    d[b[i]] = d.get(b[i], 0) + 1

count = 0
for k, v in d.items():
    if v == 1:
        count += 1
print(count)
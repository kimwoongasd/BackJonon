import sys

n = int(sys.stdin.readline())
tem = []
for _ in range(n):
    tem.append(int(sys.stdin.readline()))

d = {}
avg = round(sum(tem) / n)
tem.sort()
senter = tem[(n - 1) // 2]
for x in tem:
    d[x] = d.get(x, 0) + 1

sorted(d.items(), key=lambda x: (x[1], x[0]))
v = d.values()
m = max(v)

ls = []
for k, v in d.items():
    if v == m:
        ls.append(k)
        if len(ls) == 2:
            break

diff = tem[-1] - tem[0]
print(avg)
print(senter)
if len(ls) >= 2:
    print(ls[1])
else:
    print(ls[0])
    
print(diff)
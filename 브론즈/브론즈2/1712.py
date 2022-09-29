m = int(input())
n = int(input())

tem = []
res = 0
f = False
for i in range(m , n + 1):
    if i % (i ** (1/2)) == 0:
        tem.append(i)
        res += i
        f = True
if f:     
    print(res)
    print(min(tem))
else:
    print(-1)

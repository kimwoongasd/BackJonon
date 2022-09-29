n, l, d = map(int, input().split())
tem = [False] * (n * l + 5 * (n - 1))

for i in range(n):
    s = (l + 5) * i
    for j in range(s, s + l):
        tem[j] = True
    
    res = 0
    while res < len(tem):
        if not tem[res]:
            break
        res += d
        
print(res)

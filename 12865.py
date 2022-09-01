n, k = map(int, input().split())

res = [0] * (k + 1)

for i in range(n):
    w, v = map(int, input().split())
    
    for j in range(k, w - 1, -1):
        res[j] = max(res[j], res[j - w] + v)
        
print(max(res))
    
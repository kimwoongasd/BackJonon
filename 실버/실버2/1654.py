k, n = map(int, input().split())
tem = []
for i in range(k):
    a = int(input())
    tem.append(a)
lt = 1
rt = max(tem)

res = 0
while lt <= rt:
    t = 0
    mid = (lt + rt) // 2
    
    for i in range(k):
        t += tem[i] // mid
    
    if t >= n:
        res = mid
        lt = mid + 1
        
    else:
        rt = mid - 1
print(res)
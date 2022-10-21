n = int(input())
tem = []

for i in range(n):
    tem.append(int(input()))
    
tem.sort(reverse=True)

res = []
for i in range(n):
    res.append(tem[i] * (i + 1))
print(max(res))

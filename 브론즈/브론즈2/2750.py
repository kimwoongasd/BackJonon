n = int(input())

tem = []

for i in range(n):
    a = int(input())
    tem.append(a)
    
for i in range(n):
    for j in range(n):
        if tem[i] < tem[j]:
            tem[i], tem[j] = tem[j], tem[i]

for x in tem:
    print(x)
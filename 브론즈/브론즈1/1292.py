a, b = map(int, input().split())

tem = [0]

for i in range(1, b + 1):
    for j in range(i):
        tem.append(i)
        
s = 0

for i in range(a, b + 1):
    s += tem[i]
print(s)
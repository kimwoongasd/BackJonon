n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
d = {}

for x in a:
    d[x] = d.get(x, 0) + 1
    
for x in b:
    if x in d:
        print(d[x], end=" ")
    else:
        print(0, end=" ")
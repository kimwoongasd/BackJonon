n, m = map(int, input().split())

ls_a = []
ls_b = []

for i in range(n):
    ls_a.append(list(map(int, input().split())))

for i in range(n):
    ls_b.append(list(map(int, input().split())))
    
res = []

for i in range(n):
    tem = []
    for j in range(m):
        tem.append(ls_a[i][j] + ls_b[i][j])
    res.append(tem)

for i in res:
    for x in i:
        print(x, end=" ")
    print()
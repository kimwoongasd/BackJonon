g = int(input())

s = 1
e = 1
flag = True
while s < 100001 and e < 100001:
    total = (e ** 2) - (s ** 2)
    if total == g:
        flag = False
        print(e)
        
    if total > g:
        s += 1
    else:
        e += 1

if flag:
    print(-1)
t = int(input())

for i in range(t):
    n = int(input())
    d = {}
    for j in range(n):
        tem = list(input().split())
        if tem[1] in d:
            d[tem[1]].append(tem[0])
        else:
            d[tem[1]] = [tem[0]]
    
    count = 1
    for j in d:
        count *= (len(d[j]) + 1)
    
    print(count- 1)
    
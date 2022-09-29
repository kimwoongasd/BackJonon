n = int(input())
tem = list(map(int, input().split()))
s = int(input())

disk = 0
res = 0

for i in range(n):
    if tem[i] == 0:
        disk = 0
    elif tem[i] <= s:
        disk = s
    else:
        if tem[i] % s == 0:
            disk = s * (tem[i] // s)
        else:
            disk = s * (tem[i] // s + 1)
    
    res += disk

print(res)
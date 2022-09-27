n = int(input())
tem = list(map(int, input().split()))

b = 0
x = 0
for i in range(n):
    if i == 0:
        b += 2
        x = 2
    else:
        if tem[i] == tem[i - 1]:
            if b == 0:
                b += 2
                x = 2
            else:
                b += x * 2
                x *= 2
        else:
            b += 2
            x = 2
    
    if b >= 100:
        b = 0
        x = 0
    
print(b)
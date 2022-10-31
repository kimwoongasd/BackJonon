n = int(input())
tem = list(map(int, input().split()))
t = int(input())
tem.sort()
lt = 0
rt = n - 1
count = 0

while lt < rt:
    s = tem[lt] + tem[rt]
    if s < t:
        lt += 1
    elif s > t:
        rt -= 1
    else:
        count += 1
        lt += 1

print(count)

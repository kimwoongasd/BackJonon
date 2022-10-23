def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())

for i in range(n):
    tem = list(map(int, input().split()))
    s = 0
    for j in range(1, tem[0] + 1):
        for k in range(j + 1, tem[0] + 1):
            s += gcd(tem[j], tem[k])
    print(s)
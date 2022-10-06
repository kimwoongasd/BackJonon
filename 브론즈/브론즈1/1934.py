# 최대 공약수
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
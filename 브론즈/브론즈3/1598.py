n, m = map(int, input().split())
n -= 1
m -= 1

y = abs((n % 4) - (m % 4))
x = abs((n // 4) - (m // 4))

print(x + y)
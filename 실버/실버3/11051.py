n, k = map(int, input().split())
ch = [[0] for _ in range(1001)]
ch[1].append(1)
for i in range(2, 1001):
    for j in range(1, i + 1):
        if j == 1:
            ch[i].append(1)
        elif i == j:
            ch[i].append(1)
        else:
            ch[i].append(ch[i - 1][j] + ch[i - 1][j - 1])
print(ch[n + 1][k + 1] % 10007)

# 함수 사용, 시간단축
# from math import factorial
# n, k = map(int, input().split())
# result = factorial(n) // (factorial(k) * factorial(n - k))
# print(result % 10007)
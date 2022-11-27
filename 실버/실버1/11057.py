# 2중 for문
n = int(input())
ch = [[0] * 10 for _ in range(1001)]
ch[1] = [1] * 10
for i in range(2, n + 1):
    for j in range(10):
        ch[i][j] += ch[i - 1][j] + ch[i][j - 1]

print(sum(ch[n]) % 10007)

# 3중 for문
# n = int(input())
# ch = [[0] * 10 for _ in range(1001)]
# ch[1] = [1] * 10
# for i in range(2, n + 1):
#     for j in range(10):
#         for k in range(j, 10):
#             맨 앞자리가 i일 때 그 뒤에 올 숫자의 합
#             ch[i][j] += ch[i - 1][k]
# print(sum(ch[n]) % 10007)
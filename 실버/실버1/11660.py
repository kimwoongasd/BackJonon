import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
ch = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        ch[i][j] = ch[i][j - 1] + ch[i - 1][j] - ch[i - 1][j - 1] + arr[i - 1][j - 1]

for _ in range(m):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    print(ch[x_2][y_2] - ch[x_2][y_1 - 1] - ch[x_1 - 1][y_2] + ch[x_1 - 1][y_1 - 1])
    
# 시간 초과  
# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)

# for _ in range(m):
#     x_1, y_1, x_2, y_2 = map(int, input().split())
#     s = 0
#     for i in range(x_1 - 1, x_2):
#         s+= sum(arr[i][y_1-1:y_2])
#     print(s)
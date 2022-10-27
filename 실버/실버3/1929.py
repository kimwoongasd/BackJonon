m, n = map(int, input().split())

ch = [0] * (n + 2)
# 시간 줄이기
for i in range(2, n + 1):
    if ch[i] == 0:
        for j in range(i * 2, n + 1, i):
            ch[j] = 1
        
    if i >= m and i <= n and ch[i] == 0:
        print(i)


# for i in range(2, n + 1):

#     for j in range(i * 2, n + 1, i):
#         ch[j] = 1
        
#     if i >= m and i <= n and ch[i] == 0:
#         print(i)
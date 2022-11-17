n = int(input())
arr = list(map(int, input().split()))

ch = [1] * n
for i in range(1, n):
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            ch[i] = max(ch[i], ch[j] + 1)
ch = [0] * n

# 시간 줄인 코드
# ch[0] = 1
# for i in range(1, n):
#     t = 0
#     for j in range(i, -1, -1):
#         if arr[i] > arr[j] and ch[j] > t:
#             t = ch[j]
#     ch[i] = t + 1

print(max(ch))
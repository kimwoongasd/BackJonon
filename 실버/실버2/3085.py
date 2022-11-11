# def dfs(arr):
#     t = 1
#     for i in range(n):
#         count = 1
#         for j in range(1, n):
#             if arr[i][j] == arr[i][j - 1]:
#                 count += 1
#             else:
#                 count = 1
#             t = max(t, count)
        
#         count = 1
#         for k in range(1, n):
#             if arr[k][i] == arr[k - 1][i]:
#                 count += 1
#             else:
#                 count = 1
#             t = max(t, count)
            
#     return t

# n = int(input())
# arr = []

# for _ in range(n):
#     a = list(map(str, input()))
#     arr.append(a)
    
# res = 0
# for i in range(n):
    # for j in range(n):
        # 알파벳이 서로 다른 부분만 바꿔주기
#         if j + 1 < n and arr[i][j] != arr[i][j + 1]:
#             arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
#             ch = dfs(arr)
#             print(arr)
#             arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
#             res = max(res, ch)
            
#         if i + 1 < n and arr[i + 1][j] != arr[i][j]:
#             arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
#             ch = dfs(arr)
#             arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
#             res = max(res, ch)
# print(res)

# 바꿔주는 x, y 축만 숫자 계산
# 위의 코드보다 절반이상 빨라짐    
def dfs(arr, s_row, e_row, s_col, e_col):
    t = 1
    for i in range(s_row, e_row + 1):
        count = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                count += 1
            else:
                count = 1
            t = max(count, t)
            
    for k in range(s_col, e_col + 1):
        count = 1
        for l in range(1, n):
            if arr[l - 1][k] == arr[l][k]:
                count += 1
            else:
                count = 1
            t = max(count, t)
    return t
    
n = int(input())
arr = []

for _ in range(n):
    a = list(map(str, input()))
    arr.append(a)
    
res = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            ch = dfs(arr, i, i, j, j + 1)
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            res = max(res, ch)
            
        if i + 1 < n:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            ch = dfs(arr, i, i + 1, j, j)
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            res = max(res, ch)
print(res)
        
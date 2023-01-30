# 그리디 알고르즘
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key= lambda x : (x[1], x[0]))
cnt = 1
tem = arr[0][1]
for i in range(1, n):
    if arr[i][0] >= tem:
        tem = arr[i][1]
        cnt += 1
        
print(cnt)

# 조금 더 빠른 코드
# cnt = 0
# for x, y in arr:
#     if tem <= x:
#         tem = y
#         cnt += 1
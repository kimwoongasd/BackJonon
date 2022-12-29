import sys
input = sys.stdin.readline

# 투포인터 알고리즘
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 두 개의 포인터는 0에서 부터 시작
lt, rt = 0, 0
total = 0
d = sys.maxsize

while True:
    # 만약 총 합이 S가 넘는다면, lt를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
    if total >= s:
        total -= arr[lt]
        d = min(rt - lt, d)
        lt += 1
    
    # 만약 총합이 S를 넘지 않는다면, rt 을 오른쪽으로 한칸씩 옮기며 총합이 S를 넘을때까지 더함
    else:
        if rt == n:
            break
        total += arr[rt]
        rt += 1

if d == sys.maxsize:
    print(0)
else:
    print(d)

# 시간초과
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))

# res = 2147000000
# for i in range(n - 1):
#     total = arr[i]
#     count = 1
#     for j in range(i + 1, n):
#         if total >= s and res > count:
#             res = count
#             break
#         total += arr[j]
#         count += 1

# print(res)
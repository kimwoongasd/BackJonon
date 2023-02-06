import heapq

n = int(input())
arr = []
for _ in range(n):
    p, d = map(int, input().split())
    arr.append([p, d])

arr.sort(key=lambda x : x[1])
res = []
for x in arr:
    a, b = x[0], x[1]
    heapq.heappush(res, a)
    # 날짜보다 큰 길이면 가장 작은 값을 제거
    if len(res) > b:
        heapq.heappop(res)

print(sum(res))

# 틀림
# n = int(input())
# arr = []
# for _ in range(n):
#     p, d = map(int, input().split())
#     arr.append([p, d])

# arr.sort(reverse=True, key= lambda x :(x[1], x[0]))
# res = 0
# ch = [0] * 10001
# for x in arr:
#     a, b = x[0], x[1]
#     if ch[b] == 0:
#         res += a
#         ch[b] = 1
# print(res)
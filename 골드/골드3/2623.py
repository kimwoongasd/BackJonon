from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
num = [0] * n
for _ in range(m):
    pd = list(map(int, input().split()))
    for i in range(1, pd[0]):
        # 현재 순서에서 다음 순서로 넘어갈 숫자 추가
        arr[pd[i] - 1].append(pd[i + 1] - 1)
        # 다음 순서로 넘어갈 숫자에 +1
        num[pd[i + 1] - 1] += 1

dq = deque()
for i in range(n):
    if num[i] == 0:
        dq.append(i)
res = []
while dq:
    x = dq.popleft()
    res.append(x + 1)
    for i in arr[x]:
        num[i] -= 1
        if num[i] == 0:
            dq.append(i)

if len(res) != n:
    print(0)
else:
    for x in res:
        print(x)
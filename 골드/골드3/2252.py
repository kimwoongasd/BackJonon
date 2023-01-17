from collections import deque

# 우싱 정렬
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    # 숫자가 늘어날수록 뒤에 출력
    ch[y] += 1

dq = deque()
# 앞에 올 학생을 dq에 넣는다
for i in range(1, n + 1):
    if ch[i] == 0:
        dq.append(i)

res = []
while dq:
    x = dq.popleft()
    res.append(x)
    for i in arr[x]:
        ch[i] -= 1
        # 0이 되면 학생 순서가 되므로 dq에 추가
        if ch[i] == 0:
            dq.append(i)
print(*res)
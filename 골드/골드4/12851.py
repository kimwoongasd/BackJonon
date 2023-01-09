from collections import deque

n, k = map(int, input().split())
inf = 2174000000
arr = [inf] * 100001

dq = deque()
dq.append(n)
arr[n] = 0
count = 0
while dq:
    x = dq.popleft()
    if x == k:
        count += 1
    
    for i in (x * 2, x - 1, x + 1):
        # arr[i] == inf or arr[i] == arr[x] + 1
        # 위 조건은 한번 들렸던 곳이거나 다음 갈 곳의 시간이 작거나 같으면 경우의 수를 추가해준다.
        if 0 <= i < 100001 and (arr[i] == inf or arr[i] >= arr[x] + 1):
            arr[i] = min(arr[x] + 1, arr[i])
            dq.append(i)

print(arr[k])
print(count)
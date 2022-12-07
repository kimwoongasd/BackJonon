n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()
ch = [0] * n
# 맨 마지막 전기줄이 1일때
ch[0] = 1

for i in range(1, n):
    t = 0
    # 맨 마지막 전기줄을 기준으로 최댓값 구하기
    for j in range(i - 1, -1, -1):
        if arr[i][1] > arr[j][1] and t < ch[j]:
            t = ch[j]
    ch[i] = t + 1
print(n - max(ch))
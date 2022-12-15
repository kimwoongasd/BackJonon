n, k = map(int, input().split())

ch = [0] * (k + 1)

for i in range(n):
    w, v = map(int, input().split())
    for j in range(k, w - 1, -1):
        ch[j] = max(ch[j], ch[j - w] + v)
    print(ch)
print(max(ch))

n, k = map(int, input().split())
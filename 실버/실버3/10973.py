n = int(input())
tem = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if tem[i] < tem[i - 1]:
        for j in range(n - 1, 0, -1):
            if tem[i - 1] > tem[j]:
                tem[i - 1], tem[j] = tem[j], tem[i - 1]
                tem = tem[:i] + sorted(tem[i:], reverse=True)
                print(*tem)
                exit(0)
print(-1)
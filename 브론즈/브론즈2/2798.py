n ,m =map(int, input().split())
tem = list(map(int, input().split()))

max_res = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = tem[i] + tem[j] + tem[k]
            if s > m:
                continue
            else:
                if max_res < s:
                    max_res = s
print(max_res)
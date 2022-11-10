# pyp3로 풀림
n, m = map(int, input().split())
tree = list(map(int, input().split()))

lt = 0
rt = max(tree)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    
    c = 0
    for i in range(n):
        if tree[i] > mid:
            c += tree[i] - mid
    
    if c >= m:
        lt = mid + 1
        if res < mid:
            res = mid

    else:
        rt = mid - 1
print(res)

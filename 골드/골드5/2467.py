n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = abs(arr[0] + arr[-1])
s = 0
e = n - 1
a, b = arr[s], arr[n - 1]
while s < e:
    lt, rt = arr[s], arr[e]
    
    total = lt + rt
    
    if abs(total) < res:
        res = abs(total)
        a, b = lt, rt
        if res == 0:
            break
    
    if total < 0:
        s += 1
    
    else:
        e -= 1

print(a, b)
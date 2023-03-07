n = int(input())
arr = list(map(int, input().split()))
arr.sort()

s = 0
e = n - 1
res = abs(arr[s] + arr[e])
a, b = arr[s], arr[e]
while s < e:
    if abs(arr[s] + arr[e]) < res:
        res = abs(arr[s] + arr[e])
        a, b = arr[s], arr[e]
        
        if res == 0:
            break

    if arr[s] + arr[e] > 0:
        e -= 1
    
    else:
        s += 1

print(a, b)
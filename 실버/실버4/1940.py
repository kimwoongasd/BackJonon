n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

s = 0
e = n - 1
cnt = 0
while s < e:
    if arr[s] + arr[e] == m:
        cnt += 1
        s += 1
        e -= 1
    
    elif arr[s] + arr[e] > m:
        e -= 1
    
    else:
        s += 1

print(cnt)
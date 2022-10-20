def binary(start, end, target, arr):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in range(m):
    if binary(0, n - 1, b[i], a) is not None:
        print(1)
    else:
        print(0)

# 시간초과
# a.sort()
# for i in range(m):
#     if b[i] in a:
#         print(1)
#     else:
#         print(0)
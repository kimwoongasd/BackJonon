def binary_search(start, end, target, arr):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in range(m):
    if binary_search(0, n - 1, b[i], a) is not None:
        print(1, end=" ")
    else:
        print(0, end=" ")


# tem_1 = [0] * 10000001
# tem_2 = [0] * 10000001

# for x in a:
#     if x >= 0:
#         tem_1[x] = 1
#     else:
#         tem_2[abs(x)] = 1
        
# for y in b:
#     if y >= 0:
#         if tem_1[y] == 1:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     else:
#         if tem_2[abs(y)] == 1:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
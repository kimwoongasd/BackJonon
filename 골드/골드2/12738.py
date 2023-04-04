'''
풀이
일반적으로 LIS의 길이를 구하는 것은 dp와 이분탐색이 있다. 나는 dp만 알고있었다
1 ch에 배열의 첫번째 값을 넣어줍니다.
2 for문으로 배열의 끝까지 검사를 하게 되는데
    2-1 ch에서 가장 큰 값보다 arr[i]가 더 크다면 그대로 res에 append해줍니다.
    2-2 아니라면 res 배열에서 해당하는 숫자가 있는지 이분탐색으로 찾아보고 ch[index]에 arr[i]를 넣어줍니다.
3 ch의 길이를 출력합니다.
'''

def binary_search(start, end, target):
    if start > end:
        return start
    
    mid = (start + end) // 2
    
    if ch[mid] > target:
        return binary_search(start, mid - 1, target)
    
    elif ch[mid] == target:
        return mid
    
    else:
        return binary_search(mid + 1, end, target)

n = int(input())
arr = list(map(int, input().split()))

ch = [arr[0]]

for i in range(1, n):
    if arr[i] > ch[-1]:
        ch.append(arr[i])
    else:
        ch[binary_search(0, len(ch) - 1, arr[i])] = arr[i]

print(len(ch))

# 이분 탐색해주는 라이브러리 이용
# from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

# input()
# A = list(map(int, input().split()))
# dp = []

# for i in A:
#     k = bisect_left(dp, i) #자신이 들어갈 위치 k
#     if len(dp) <= k: #i가 가장 큰 숫자라면
#         dp.append(i)
#     else:
#         dp[k] = i #자신보다 큰 수 중 최솟값과 대체
# print(len(dp))

#  시간초과
# n = int(input())
# arr = list(map(int, input().split()))

# ch = [0] * n
# ch[0] = 1

# for i in range(1, n):
#     t = 0
#     for j in range(i, -1, -1):
#         if arr[i] > arr[j] and t < ch[j]:
#             t = ch[j]
#     ch[i] = t + 1

# print(max(ch))
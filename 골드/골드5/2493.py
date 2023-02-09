'''
풀이
오른쪽 값부터 하면 시간초과가 나기때문에 왼쪽값부터 처리해야한다
stack = [ ]  -> 최댓값을 저장할 스택
res = [ ] -> 수신 탑 인덱스 저장
1. stack이 비어있다면 큰값이 없는 것이기 떄문에 0을 추가한다
2. stack이 있는 상황에서 stack값이 더 크다면 res에 인덱스를 추가해준다
'''
n = int(input())
arr = list(map(int, input().split()))
stack = []
res = []
for i in range(n):
    while stack:
        if stack[-1][1] > arr[i]:
            res.append(stack[-1][0] + 1)
            break
            
        else:
            stack.pop()
    
    if not stack:
        res.append(0)
    stack.append([i, arr[i]])
    
print(*res)

# 시간초과
# n = int(input())
# arr = list(map(int, input().split()))
# res = []
# for i in range(n - 1, -1, -1):
#     for j in range(i - 1, -1, -1):
#         if arr[i] < arr[j]:
#             res.append(j + 1)
#             break
#     else:
#         res.append(0)
# print(*res[::-1])